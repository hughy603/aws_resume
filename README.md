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
        DJANGO_AWS_SECRET_ACCESS_KEY: "fdsafdasB"
        DJANGO_ADMIN_URL: "resumeadminportal"
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
eb ssh

## Create EB Storage Bucket
Go to https://console.aws.amazon.com/s3/home?region=us-east-1#
Create a bucket
Add COORS Configuration
Add bucket policy
```
{
  "Version": "2008-10-17",
  "Statement": [
    {
      "Sid": "PublicReadForGetBucketObjects",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::rice-adam-resume/*"
    },
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::539495328509:user/rice.adam"
      },
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::rice-adam-resume",
        "arn:aws:s3:::rice-adam-resume/*"
      ]
    }
  ]
}
```
