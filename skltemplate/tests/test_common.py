import pytest

from sklearn.utils.estimator_checks import check_estimator
from .._list_estimators import list_all_estimators

@pytest.mark.parametrize(
    "EstimatorName, Estimator", list_all_estimators()
)
def test_all_estimators(EstimatorName, Estimator):
    return check_estimator(Estimator)
