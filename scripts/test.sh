set -e

# Get into a temp directory to run test from the installed scikit learn and
# check if we do not leave artifacts
mkdir -p $TEST_DIR
# We need the setup.cfg for the nose settings
cp setup.cfg $TEST_DIR
cd $TEST_DIR

python --version
python -c "import numpy; print('numpy %s' % numpy.__version__)"
python -c "import scipy; print('scipy %s' % scipy.__version__)"

# Skip tests that require large downloads over the network to save bandwidth
# usage as travis workers are stateless and therefore traditional local
# disk caching does not work.
export SKLEARN_SKIP_NETWORK_TESTS=1

if [[ "$COVERAGE" == "true" ]]; then
    nosetests -s --with-coverage --with-timer --timer-top-n 20 sklstub
else
    nosetests -s --with-timer --timer-top-n 20 sklstub
fi
