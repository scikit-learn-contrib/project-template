from sklearn.utils.estimator_checks import check_estimator
from sklstub.stub import StubEstimator

def test_common():
    return check_estimator(StubEstimator)
