
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

