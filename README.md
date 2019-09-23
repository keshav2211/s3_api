# S3 API

A simple API to create bucket and manage objects in **AWS S3**.
Utilizes Ansible module [aws_s3]([https://docs.ansible.com/ansible/2.4/aws_s3_module.html](https://docs.ansible.com/ansible/2.4/aws_s3_module.html)) as a client to AWS S3.

Swagger is used for API UI.

## Deployment options
### Local
1. Install python3 (preferably use venv)
2. Clone the repo
3. pip install -r requirements
4. python app.py

### Docker
1. Clone the repo 
2. docker build -t "s3_api" .
3. docker run -p 5000:5000 s3_api:latest

## Authentication
Accepts access_key and secret_key in json body. 
>It is required to pass these keys in all requests.

## Create bucket in S3

Create a bucket in S3 by providing a DNS compliant bucket name and region.

## Add object to bucket

Add object to bucket by providing bucket name, source path of object(file) on API server, object key.

> **Limitation**: *Only objects(files) existing on API  server can be uploaded as ansible module(aws_s3) accepts path to source file as input. Some test files included in test_objects dir in the repo.*

`eg. json:`
>{\
  "src": "/usr/share/s3_api/test_objects/text_file.txt",\
  "key": "text_file",\
  "access_key": "REDACTED",\
  "secret_key": "REDACTED"\
}

## Update object

Update and existing object by providing bucket name, source path of object(file) on API server, object key.

## Delete object

Delete an object by providing bucket name and object key.