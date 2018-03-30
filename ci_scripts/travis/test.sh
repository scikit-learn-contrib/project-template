set -e

# Get into a temp directory to run test from the installed scikit learn and
# check if we do not leave artifacts
mkdir -p $TEST_DIR
cp setup.cfg $TEST_DIR
cd $TEST_DIR

TEST_CMD="pytest --showlocals --pyargs"
if [[ "$COVERAGE" == "true" ]]; then
    TEST_CMD="$TEST_CMD --cov $MODULE"
fi
$TEST_CMD $MODULE
