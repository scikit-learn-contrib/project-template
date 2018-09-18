from .template import (TemplateEstimator, TemplateClassifier,
                       TemplateTransformer)
from . import template
from ._version import __version__

__all__ = ['TemplateEstimator', 'TemplateClassifier',
           'TemplateTransformer', 'template',
           '__version__']
