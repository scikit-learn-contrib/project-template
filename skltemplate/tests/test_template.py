"""This file will just show how to write tests for the template classes."""
import numpy as np
import pytest
from sklearn.datasets import load_iris
from sklearn.utils._testing import assert_allclose, assert_array_equal

from skltemplate import TemplateClassifier, TemplateEstimator, TemplateTransformer

# Authors: scikit-learn-contrib developers
# License: BSD 3 clause


@pytest.fixture
def data():
    return load_iris(return_X_y=True)


def test_template_estimator(data):
    """Check the internals and behaviour of `TemplateEstimator`."""
    est = TemplateEstimator()
    assert est.demo_param == "demo_param"

    est.fit(*data)
    assert hasattr(est, "is_fitted_")

    X = data[0]
    y_pred = est.predict(X)
    assert_array_equal(y_pred, np.ones(X.shape[0], dtype=np.int64))


def test_template_transformer(data):
    """Check the internals and behaviour of `TemplateTransformer`."""
    X, y = data
    trans = TemplateTransformer()
    assert trans.demo_param == "demo"

    trans.fit(X)
    assert trans.n_features_in_ == X.shape[1]

    X_trans = trans.transform(X)
    assert_allclose(X_trans, np.sqrt(X))

    X_trans = trans.fit_transform(X)
    assert_allclose(X_trans, np.sqrt(X))


def test_template_classifier(data):
    """Check the internals and behaviour of `TemplateClassifier`."""
    X, y = data
    clf = TemplateClassifier()
    assert clf.demo_param == "demo"

    clf.fit(X, y)
    assert hasattr(clf, "classes_")
    assert hasattr(clf, "X_")
    assert hasattr(clf, "y_")

    y_pred = clf.predict(X)
    assert y_pred.shape == (X.shape[0],)
