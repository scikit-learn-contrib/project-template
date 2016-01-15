from sklearn.utils.estimator_checks import check_estimator
from skldemo.demo import DemoEstimator

def test_common():
    return check_estimator(DemoEstimator)
