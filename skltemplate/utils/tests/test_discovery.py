# Authors: scikit-learn-contrib developers
# License: BSD 3 clause

import pytest

from skltemplate.utils.discovery import all_displays, all_estimators, all_functions


def test_all_estimators():
    estimators = all_estimators()
    assert len(estimators) == 3

    estimators = all_estimators(type_filter="classifier")
    assert len(estimators) == 1

    estimators = all_estimators(type_filter=["classifier", "transformer"])
    assert len(estimators) == 2

    err_msg = "Parameter type_filter must be"
    with pytest.raises(ValueError, match=err_msg):
        all_estimators(type_filter="xxxx")


def test_all_displays():
    displays = all_displays()
    assert len(displays) == 0


def test_all_functions():
    functions = all_functions()
    assert len(functions) == 3
