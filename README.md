[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/mashi/codecov-validator.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/mashi/codecov-validator/context:python)
[![codecov](https://codecov.io/gh/mashi/codecov-validator/branch/main/graph/badge.svg?token=WBOQOGFC51)](https://codecov.io/gh/mashi/codecov-validator)
[![github-actions](https://github.com/mashi/codecov-validator/actions/workflows/ci.yml/badge.svg)](https://github.com/mashi/codecov-validator/actions)
[![Documentation Status](https://readthedocs.org/projects/codecov-validator/badge/?version=latest)](https://codecov-validator.readthedocs.io/en/latest/?badge=latest)


# Description
Validates the `codecov.yml` configuration file.

This python package executes the equivalent of the `curl` command described in the
[codecov documentation](https://docs.codecov.io/docs/codecov-yaml), and it can be
integrated in the [pre-commit](https://github.com/pre-commit/pre-commit).

This package was inspired by [gitlab-lint](https://pypi.org/project/gitlab-lint/),
package that checks `.gitlab-ci.yml` configuration file.


## Usage
The recommended use is to add in the `.pre-commit-config.yaml` file
```
- repo: https://github.com/mashi/codecov-validator
  rev: v1.0.0  # replace by any tag version >= 1.0.0 available
  hooks:
    - id: ccv
      # args: [--filename, .codecov.yml]  # example with arguments
```

In this way, the `codecov.yml` file is checked before `commit` and prevents the
user from including invalid files in the version control.


## Software and Tools
The development uses:
1. Version control with git to track changes.

1. A pre-commit to maintain the quality of the code. It helps identify issues,
for example, code formatting, *before* files are added to the version control.
Check the `.pre-commit-config.yaml` for the complete list of verifications.

1. The code documentation is generated automatically from the docstrings and
exported to readthedocs (click on docs the badge above).

1. Here, CI/CD methods are implemented using GitHub actions configured inside
the `.github` folder. The CI process is executed after code changes and includes
    1. code formatting check,
    1. running tests for different python versions,
    1. and package build check.

    The CD process is triggered by new tags in this repository:
    1. tests are executed,
    1. the package is built,
    1. and the new release is upload to pypi.

1. For maintenance:
    1. the renovatebot is configured to keep packages up to date.
    1. Scheduled tests are configured to periodically perform tests
    and builds.


## Instructions (Development)
The code is developed inside a virtual environment with the packages from the
`requirements.txt` file:
```
python3 -m venv .venv
source .venv/bin/activate
pip install wheel
pip install -r requirements.txt
pre-commit install
```


To execute tests:
```
python -m unittests discover -b
```


To generate the documentation, install the packages and call sphinx:
```
python3 -m venv .venv
source .venv/bin/activate
pip install wheel
pip install -r docs/requirements-doc.txt
sphinx-build -E -b html docs/source docs/_build
```
After the end of the build process, open the `docs/_build/index.html` file.
