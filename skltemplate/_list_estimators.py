"""
This is a helper module to list all estimators within a project 
"""
import inspect
import pkgutil
from pathlib import Path
from operator import itemgetter
from importlib import import_module
import os

from sklearn.base import (
    BaseEstimator,
    ClassifierMixin,
    RegressorMixin,
    TransformerMixin,
    ClusterMixin,
)

import sklearn


SK_VERSION = sklearn.__version__[:4]

TYPE_FILTERS = dict(
    classifier=ClassifierMixin,
    regressor=RegressorMixin,
    transformer=TransformerMixin,
    cluster=ClusterMixin,
)

def is_abstract(c):
    if not(hasattr(c, '__abstractmethods__')):
        return False
    if not len(c.__abstractmethods__):
        return False
    return True

def is_estimator(obj_name, obj):
    is_est = issubclass(obj, BaseEstimator) and obj_name != 'BaseEstimator'
    is_est &= (not is_abstract(obj))
    return is_est

def list_all_estimators(module_name='skltemplate', type_filter=None):
    all_classes = []
    modules_to_ignore = {"tests", "externals", "setup", "conftest"}
    root = str(Path(__file__).parent.parent)  # sklearn package
    # Ignore deprecation warnings triggered at import time and from walking
    # packages
    #root = os.path.join(root, module_name)
    prefix = module_name + '.'
    for _, modname, _ in pkgutil.walk_packages(path=[root], prefix=prefix):
        if modname.startswith(module_name + '.' + module_name):
            modname = modname[len(prefix):]  # remove starting prefix
        mod_parts = modname.split(".")
        if (any(part in modules_to_ignore for part in mod_parts) or '._' in modname):
            continue
        module = import_module(modname)
        classes = inspect.getmembers(module, inspect.isclass)
        classes = [(name, est_cls) for name, est_cls in classes
                    if not name.startswith("_")]

        all_classes.extend(classes)

    all_classes = set(all_classes)

    estimators = [c for c in all_classes if is_estimator(*c)]

    if type_filter is not None:
        type_filter = list(type_filter) if isinstance(type_filter, list) else [type_filter]
        if set(type_filter).isdisjoint(TYPE_FILTERS.keys()):
            raise ValueError("Parameter type_filter must be {}"
                .format(' or '.join(TYPE_FILTERS.keys())))

        filtered_estimators = []

        for name, mixin in TYPE_FILTERS.items():
            if name in type_filter:
                type_filter.remove(name)
                filtered_estimators.extend(
                    [est for est in estimators if issubclass(est[1], mixin)]
                )
        estimators = filtered_estimators

    if SK_VERSION >= '0.23':
        # from sklearn 0.23 check_estimator takes an instance as input
        estimators = [(_name, _cls()) for _name, _cls in estimators]

    # drop duplicates, sort for reproducibility
    # itemgetter is used to ensure the sort does not extend to the 2nd item of
    # the tuple
    return sorted(set(estimators), key=itemgetter(0))
