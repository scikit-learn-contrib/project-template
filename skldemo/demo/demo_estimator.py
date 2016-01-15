from sklearn.base import BaseEstimator
from sklearn.utils import check_X_y, check_array

class DemoEstimator(BaseEstimator):
    def __init__(self, demo_param='demo_param'):
        self.demo_param = 'demo_param'

    def fit(self, X, y):
        X, y = check_X_y(X, y)
        return self

    def predict(self, X):
        X = check_array(X)
        return X[:, 0]