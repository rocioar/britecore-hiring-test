BriteCoreHiringTest
===================

Brite Core Hiring test project

![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg "Built with Cookiecutter Django")

License: GPLv3

Test coverage
-------------

To run the tests, check your test coverage, and generate an HTML coverage report:

```
  $ coverage run -m pytest
  $ coverage html
  $ open htmlcov/index.html
```

### Running tests with py.test

```
  $ pytest
```

Development environment
-----------------------

First create the virtualenviroment:

```
  $ mkvirtualenv britecore -p python3
```

Install the requirements:
  
```
  $ pip install -r requirements/local.txt
```

Create the database:

```
  $ python manage.py migrate
```

Run it:

```  
  $ python manage.py runserver
```

Deployment
----------

This application is prepared to be deployed using AWS Lambda and zappa.

Install `zappa`:

```
  $ pip install zappa
```

Install `aws-cli` to run cloudformation template:

```
  $ pip install aws-cli
```

Configure `aws-cli`

```
  $ aws configure
```

Edit the `vpc_to_rds.json` and setup the `DBPassword` parameter.

Run the cloudformation template using `aws-cli`:

```
  $ aws cloudformation create-stack --stack-name britecorestack --template-body file://vpc_for_rds.json --parameters
```

Wait for it to run.

Check the outputs section using the `describe-stacks` command:

```
  $ aws cloudformation describe-stacks --stack-name britecorestack
```

On the outputs section it should show you something like this:

```
  {
      "OutputKey": "DBInstanceAddress",
      "OutputValue": "bd7zx47f2x1rjg.cobxtajiks3q.us-east-1.rds.amazonaws.com",
      "Description": "PostgreSQL RDS instance IP"
  }
```

We will use the db instance `OutputValue` to define the database that Django is going to use, on the zappa_settings.json file.

Move `zappa_settings.json.example` to `zappa_settings.json`:

```
  $ mv zappa_settings.json.example zappa_settings.json
```

Update `zappa_settings.json` with the correct values for the environment variables:

```python
  "DJANGO_SECRET_KEY": "" # Create a secret key for your django instance
  "DATABASE_URL": "" # Use the database value extracted from the cloudformation outputs here
  "DJANGO_ALLOWED_HOSTS": "" # Indicate the domain where it's going to run 
```

The project needs an s3 bucket to run, create the bucket and setup the following variables:

```python
  "DJANGO_AWS_ACCESS_KEY_ID": ""
  "DJANGO_AWS_SECRET_ACCESS_KEY": ""
  "DJANGO_AWS_STORAGE_BUCKET_NAME": "britecoredjango"
```

Deploy using `zappa`:

```
  $ zappa deploy prod
```
