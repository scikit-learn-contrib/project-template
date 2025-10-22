# Authors: scikit-learn-contrib developers
# License: BSD 3 clause

from sklearn import __version__

from ._template import TemplateClassifier, TemplateEstimator, TemplateTransformer

__all__ = [
    "TemplateEstimator",
    "TemplateClassifier",
    "TemplateTransformer",
    "__version__",
]
