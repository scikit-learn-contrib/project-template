.. project-template documentation master file, created by
   sphinx-quickstart on Mon Jan 18 14:44:12 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:notoc:

#############################################
Project template for `scikit-learn` extension
#############################################

**Date**: |today| **Version**: |version|

**Useful links**:
`Source Repository <https://github.com/scikit-learn-contrib/project-template>`__ |
`Issues & Ideas <https://github.com/scikit-learn-contrib/project-templatek/issues>`__ |

This is the documentation for the `project-template` to help at extending
`scikit-learn`. It provides some information on how to build your own custom
`scikit-learn` compatible estimators as well as a template to package them.


.. grid:: 1 2 2 2
    :gutter: 4
    :padding: 2 2 0 0
    :class-container: sd-text-center

    .. grid-item-card:: Getting started
        :img-top: _static/img/index_getting_started.svg
        :class-card: intro-card
        :shadow: md

        Information regarding this template and how to modify it for your own project.

        +++

        .. button-ref:: quick_start
            :ref-type: ref
            :click-parent:
            :color: secondary
            :expand:

            To the getting started guideline

    .. grid-item-card::  User guide
        :img-top: _static/img/index_user_guide.svg
        :class-card: intro-card
        :shadow: md

        An example of narrative documentation. Here, we will explain how to create your
        own `scikit-learn` estimator.

        +++

        .. button-ref:: user_guide
            :ref-type: ref
            :click-parent:
            :color: secondary
            :expand:

            To the user guide

    .. grid-item-card::  API reference
        :img-top: _static/img/index_api.svg
        :class-card: intro-card
        :shadow: md

        An example of API documentation. This is an example how to use `sphinx` to
        automatically generate reference API page.

        +++

        .. button-ref:: api
            :ref-type: ref
            :click-parent:
            :color: secondary
            :expand:

            To the reference guide

    .. grid-item-card::  Examples
        :img-top: _static/img/index_examples.svg
        :class-card: intro-card
        :shadow: md

        A set of examples. It complements the User Guide and it is the right place to
        show how to use your compatible estimator.

        +++

        .. button-ref:: general_examples
            :ref-type: ref
            :click-parent:
            :color: secondary
            :expand:

            To the gallery of examples


.. toctree::
    :maxdepth: 3
    :hidden:
    :titlesonly:

    quick_start
    user_guide
    api
    auto_examples/index
