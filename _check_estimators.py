import inspect

import sklearn
from sklearn.utils.estimator_checks import check_estimator
from skltemplate._list_estimators import list_all_estimators


OK = '\x1b[42m[ OK ]\x1b[0m'
FAIL = "\x1b[41m[FAIL]\x1b[0m"

if __name__ == '__main__':
    estimators = list_all_estimators()

    for est_name, est in estimators:
        checks = check_estimator(est, generate_only=True)
        for arg, check in checks:
            check_name = check.func.__name__  # unwrap partial function
            desc = '{} === {}'.format(est_name, check_name)
            try:
                check(arg)
                print(OK, desc)
            except Exception as e:
                print(FAIL, desc, e)
