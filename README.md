# S3 API

A simple API to create bucket and manage objects in **AWS S3**.
Utilizes Ansible module [aws_s3](https://docs.ansible.com/ansible/2.4/aws_s3_module.html) as a client to AWS S3.

Swagger is used for API UI.

## Deployment options
### Local
1. Install python3 (preferably use venv)
2. Clone the repo
3. cd to repo
4. pip install -r requirements
5. python app.py
5. http://127.0.0.1:5000/

### Docker
1. Clone the repo
2. cd to repo
3. docker build -t s3_api .
4. docker run -p 5000:5000 s3_api:latest
5. http://127.0.0.1:5000/

## Authentication
Accepts access_key and secret_key in json body. 
>It is required to pass these keys in all requests.

## API ENDPOINTS

### POST /S3/buckets

Create a bucket in S3 by providing a DNS compliant bucket name and region.

### POST /S3/bucket/{bucket_name}/objects

Add object to bucket by providing bucket name, source path of object(file) on API server, object key.

> **Limitation**: *Only objects(files) existing on API  server can be uploaded as ansible module(aws_s3) accepts path to source file as input. Some test files included in test_objects dir in the repo.*

`eg. json:`
>{\
  "src": "/usr/share/s3_api/test_objects/text_file.txt",\
  "key": "text_file",\
  "access_key": "REDACTED",\
  "secret_key": "REDACTED"\
}

### PUT /S3/bucket/{bucket_name}/object/{key}

Update an existing object by providing bucket name, source path of object(file) on API server, object key.

### DELETE /S3/bucket/{bucket_name}/object/{key}

Delete an object by providing bucket name and object key.