.. _quick_start:

###############
Getting started
###############

This package serves as a skeleton package aiding at developing compatible
scikit-learn contribution.

Creating your own scikit-learn contribution package
===================================================

Download and setup your repository
----------------------------------

To create your package, you need to clone the ``project-template`` repository:

.. prompt:: bash $

  git clone https://github.com/scikit-learn-contrib/project-template.git

Before to reinitialize your git repository, you need to make the following
changes. Replace all occurrences of ``skltemplate``, ``sklearn-template``, or
``project-template`` with the name of you own project. You can find all the
occurrences using the following command:

.. prompt:: bash $

  git grep skltemplate
  git grep sklearn-template
  git grep project-template

To remove the history of the template package, you need to remove the `.git`
directory:

.. prompt:: bash $

  rm -rf .git

Then, you need to initialize your new git repository:

.. prompt:: bash $

  git init
  git add .
  git commit -m 'Initial commit'

Finally, you create an online repository on GitHub and push your code online:

.. prompt:: bash $

  git remote add origin https://github.com/your_remote/your_contribution.git
  git push origin main

Develop your own scikit-learn estimators
----------------------------------------

.. _check_estimator: http://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator
.. _`Contributor's Guide`: http://scikit-learn.org/stable/developers/
.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _PEP257: https://www.python.org/dev/peps/pep-0257/
.. _NumPyDoc: https://github.com/numpy/numpydoc
.. _doctests: https://docs.python.org/3/library/doctest.html

You can modify the source files as you want. However, your custom estimators
need to pass the check_estimator_ test to be scikit-learn compatible. We provide a
file called `test_common.py` where we run the checks on our custom estimators.

You can refer to the :ref:`User Guide <user_guide>` to help you create a compatible
scikit-learn estimator.

In any case, developers should endeavor to adhere to scikit-learn's
`Contributor's Guide`_ which promotes the use of:

* algorithm-specific unit tests, in addition to ``check_estimator``'s common
  tests;
* PEP8_-compliant code;
* a clearly documented API using NumpyDoc_ and PEP257_-compliant docstrings;
* references to relevant scientific literature in standard citation formats;
* doctests_ to provide succinct usage examples;
* standalone examples to illustrate the usage, model visualisation, and
  benefits/benchmarks of particular algorithms;
* efficient code when the need for optimization is supported by benchmarks.

Managing your local and continuous integration environment
----------------------------------------------------------

Here, we set up for you an repository that uses `pixi`. The `pixi.toml` file defines
the packages and tasks to be run that we will present below. You can refer to the
following documentation link to install `pixi`: https://pixi.sh/latest/#installation

Once done, you can refer to the documentation to get started but we provide the
command below to interact with the main task requested to develop your package.

Edit the documentation
----------------------

.. _Sphinx: http://www.sphinx-doc.org/en/stable/

The documentation is created using Sphinx_. In addition, the examples are
created using ``sphinx-gallery``. Therefore, to generate locally the
documentation, you can leverage the following `pixi` task:

.. prompt:: bash $

  pixi run build-doc

The documentation is made of:

* a home page, ``doc/index.rst``;
* an API documentation, ``doc/api.rst`` in which you should add all public
  objects for which the docstring should be exposed publicly.
* a User Guide documentation, ``doc/user_guide.rst``, containing the narrative
  documentation of your package, to give as much intuition as possible to your
  users.
* examples which are created in the `examples/` folder. Each example
  illustrates some usage of the package. the example file name should start by
  `plot_*.py`.

Local testing
-------------

To run the tests locally, you can use the following command:

.. prompt:: bash $

  pixi run test

It will use `pytest` under the hood to run the package tests.

In addition, you have a linter task to check the code consistency in terms of style:

.. prompt:: bash $

  pixi run lint

Activating the development environment
--------------------------------------

In the case that you don't want to use the `pixi run` commands and directly interact
with the usual python tools, you can activate the development environment:

.. prompt:: bash $

  pixi shell -e dev

This will activate an environment containing the dependencies needed to run the linters,
tests, and build the documentation. So for instance, you can run the tests with:

.. prompt:: bash $

  pytest -vsl skltemplate

In this case, you can even use pre-commit before using git. You will need to initialize
it with:

.. prompt:: bash $

  pre-commit install

Setup the continuous integration
--------------------------------

The project template already contains configuration files of the continuous
integration system. It leverage the above pixi commands and run on GitHub Actions.
In short, it will:

* run the tests on the different platforms (Linux, MacOS, Windows) and upload the
  coverage report to codecov.io;
* check the code style (linter);
* build the documentation and deploy it automatically on GitHub Pages.

Publish your package
====================

.. _PyPi: https://packaging.python.org/tutorials/packaging-projects/
.. _conda-forge: https://conda-forge.org/

You can make your package available through PyPi_ and conda-forge_. Refer to
the associated documentation to be able to upload your packages such that
it will be installable with ``pip`` and ``conda``.
