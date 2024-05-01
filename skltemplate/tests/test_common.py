"""This file shows how to write test based on the scikit-learn common tests."""

from sklearn.utils.estimator_checks import parametrize_with_checks

from skltemplate import TemplateClassifier, TemplateEstimator, TemplateTransformer


# parametrize_with_checks allows to get a generator of check that is more fine-grained
# than check_estimator
@parametrize_with_checks([TemplateEstimator(), TemplateTransformer(), TemplateClassifier()])
def test_estimators(estimator, check, request):
    """Check the compatibility with scikit-learn API"""
    check(estimator)
