set -e

PYTHON_VERSION=${PYTHON_VERSION:-3.4}

pip install --upgrade setuptools pip
pip install --upgrade pylint pytest pytest-pylint pytest-runner
pip install termcolor
python setup.py develop
python -m pytest  # Run the tests without IPython.
pip install ipython
python -m pytest  # Now run the tests with IPython.
pylint fsos
# Run type-checking, excluding files that define or use py3 features in py2.
pytype