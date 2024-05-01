# Authors: scikit-learn-contrib developers
# License: BSD 3 clause

from skltemplate.utils.discovery import all_displays, all_estimators, all_functions


def test_all_estimators():
    estimators = all_estimators()
    assert len(estimators) == 3


def test_all_displays():
    displays = all_displays()
    assert len(displays) == 0


def test_all_functions():
    functions = all_functions()
    assert len(functions) == 3
