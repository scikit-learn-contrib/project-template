import pytest

from sklearn.utils.estimator_checks import check_estimator

from HQC import HQC


@pytest.mark.parametrize(
    "Estimator", [HQC]
)
def test_all_estimators(Estimator):
    return check_estimator(Estimator)
