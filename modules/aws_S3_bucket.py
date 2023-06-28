#!/bin/python3
# Description: this module happen independently from other modules 


import boto3
import logging
import os
## Create AWS S3 bucket using python boto3

# Upload a file from local system.
def list_bucket():
    # Create bucket
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        if response:
            print('Buckets exists..')
            for bucket in response['Buckets']:
                print(f' {bucket["Name"]}')

    except Exception as e:
        logging.error(e)
def upload_file(file_name, bucket, object_name=None):
  # Create 
## Create AWS S3 bucket using python boto3
## Create AWS S3 bucket using python boto3
## Create AWS S3 bucket using python boto3
## Create AWS S3 bucket using python boto3
