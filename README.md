# resume
A resume written in Django and hosted on aws.  It combines the following
*   https://realpython.com/blog/python/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/

    How to deploy DJango on AWS

*   https://github.com/pydanny/cookiecutter-django

    DJango Cookie Cutter Configuration

# Secret Settings
To deploy this file to AWS, create .ebextensions/00_secrets.config with the following variables
```
option_settings:
    "aws:elasticbeanstalk:application:environment":
        DJANGO_SECRET_KEY: "Django's Secret Key"
        DJANGO_AWS_ACCESS_KEY_ID: "AWS Access Key From IAM"
        DJANGO_AWS_SECRET_ACCESS_KEY: "OLEvohnnPfKmMA7qlxlb5Bt+6d2QzF6SQ7jiQnLB"
        DJANGO_ADMIN_URL: "blogadminportal"
```


# AWS Virtual Environment Setup

## Install Requirements
deactivate
workon resume
###### Pillow Requirements
sudo yum install zlib zlib-devel
sudo yum install libjpeg-turbo libjpeg-turbo-devel

pip install -r requirements/local.txt

## Setup Databse
sudo -u postgres createuser -D -A -P resume
sudo -u postgres createdb -O resume resume

## Create links to environment config
ln -s `pwd`/config/postactivate ~/.virtualenvs/resume/bin/postactivate

## Create EB Instance
eb init
eb create
eb open
  Go to configuration -> Data Tier -> Add new RDS Instance
eb deploy
