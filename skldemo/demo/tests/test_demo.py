import numpy as np
from numpy.testing import assert_almost_equal

from skldemo.demo import DemoEstimator


def test_demo():
    X = np.random.random((100, 10))
    estimator = DemoEstimator()
    estimator.fit(X, X[:, 0])
    assert_almost_equal(estimator.predict(X), X[:, 0])