
#User Guide

**sklearn-stub** is a template project for [scikit-learn](http://scikit-learn.org/) 
compatible extensions.
It is aimed to aid development of `scikit-learn` comptatible algorithms. It
comes pre-packaged with unit tests, a documentation website and easy to setup
continuous integration. Conforming to the template's structure will allow users
to use your library just like scikit-learn` packages. The idea is to let
programmer focus on writing code while unit tests, documentation and continuous
integration can be setup with minimal changes.


## Installation and Usage
The package by itself comes with a single module and an estimator. Before
installing the module you will need `numpy` and `scipy`.
To install the module execte.
```shell
$ python setup.py install
```
If the installation is successful you should be able to execute the following in Python
```python
>>> from sklstub.stub import StubEstimator
>>> estimator = StubEstimator()
>>> estimator.fit(np.arange(10), np.arange(10))
```

`StubEstimator` by itself does nothing useful, but it serves as an example of
how other Estimators should be written. It also comes with its own unit
tests under `sklstub/tests`.

## Creating your own library
### 1. Forking
Fork the project from its [Github Source Page](https://github.com/vighneshbirodkar/sklearn-stub). You
might also want to rename from the project settings page.

### 2. Modifying the Source
You are free to modify the source as you want, but at the very least, all your estimators 
pass the `check_estimator` test to be scikit-learn compatible. Rename the project to 

### 3. Modifying the Documentation
The documentation is located under the `doc/` folder and is built using [sphinx](http://www.sphinx-doc.org/en/stable/).
To build the documentation locally, ensure that you have `sphinx` by executing
```shell
$ pip install sphinx
```
The documentation contains a home page (`doc/index.rst`) and an API documentation page (`api.rst`).
Sphinx allows you to automcatically document your modules and classes by using the `autodoc`
directive. You can either document all your modules in `api.rst` or document them in seperate
pages and link them. For more information visit the [Sphinx Documentation](http://www.sphinx-doc.org/en/stable/contents.html)

to build the documentation locally execute
```shell
cd doc
make html
```

### 4. Setting up Travis CI
[TravisCI](https://travis-ci.org/) allows you to continuously build and test your code from Github
to ensure that no code-breaking changes are pushed. After you sign up and authourize TravisCI, 
add your new repository to TravisCI so that it can start building it. The `travis.yml` file
already contains the configuration required for Travis to build the project.


