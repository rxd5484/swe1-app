# Django Polls — SWE1

[![Build Status](https://app.travis-ci.com/rxd5484/swe1-app.svg?branch=main)](https://app.travis-ci.com/github/rxd5484/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/rxd5484/swe1-app/badge.svg?branch=main)](https://coveralls.io/github/rxd5484/swe1-app?branch=main)

This is the Django polls application from Homework 1, deployed using AWS Elastic Beanstalk. Homework 2 adds automated code-formatting checks, linting, Django tests, coverage reporting, and deployment after successful CI builds.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
python manage.py migrate
python manage.py runserver
```

Visit http://127.0.0.1:8000/polls/.

## Run the checks

```bash
black --check .
flake8 .
python manage.py check
coverage run --source=polls manage.py test polls
coverage report -m
```

To fix formatting locally, run `black .` and commit the changes.

## CI and deployment setup

1. Activate this GitHub repository at https://app.travis-ci.com/ and enable push and pull-request builds.
2. Add this public GitHub repository to https://coveralls.io/ so coverage reports can be published.
3. In Travis **Repository settings → Environment Variables**, set `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_EB_S3_BUCKET`. The bucket must exist in `us-east-2` and be accessible by the deployment IAM user/role.
4. Configure the IAM deployment credentials for the existing Elastic Beanstalk application `swe1-app` and environment `swe1-app-env` in `us-east-2`. Never commit credentials.
5. After Travis reports a CI status on a pull request, configure branch protection/rulesets on `main` to **require status checks to pass before merging**. Select the actual Travis check name shown on GitHub.
6. Passing pull-request builds validate the code without deploying; passing builds on `main` deploy to Elastic Beanstalk.

The badges may initially show unknown status until Travis and Coveralls are activated.
