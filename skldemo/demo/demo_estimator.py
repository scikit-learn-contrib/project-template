from sklearn.base import BaseEstimator

class DemoEstimator(BaseEstimator):
    def __init__(self, demo_param='demo_param'):
        self.demo_param = 'demo_param'

    def fit(self, X, y):
        return self

    def predict(self, X):
        return X[:, 0]