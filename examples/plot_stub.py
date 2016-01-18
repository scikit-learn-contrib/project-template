"""
=======================
Plotting Stub Estimator
=======================

An example plot of StubEstimator
"""
import numpy as np
from sklstub.stub import StubEstimator
from matplotlib import pyplot as plt

X = np.arange(100).reshape(100, 1)
y = np.zeros((100, ))
estimator = StubEstimator()
estimator.fit(X, y)
plt.plot(estimator.predict(X))
plt.show()