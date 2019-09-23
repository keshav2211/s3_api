from flask import Flask
from flask_restplus import Api, Resource, fields
from s3.bucket import Bucket

app = Flask(__name__)
api = Api(app=app,
          version='1.0',
          title='S3 API',
          description='API to manage S3 objects'
          )
ns = api.namespace('S3', description='S3 operations')

bucket = api.model('bucket', {
    'name': fields.String(description='Bucket name', required=True),
    'region': fields.String(description='AWS region code', required=False),
    'access_key': fields.String(description='AWS access key', required=False),
    'secret_key': fields.String(description='AWS secret key', required=False)
})

s3_new_object = api.model('s3_new_object', {
    'key': fields.String(description='keyname of the object inside the bucket', required=True),
    'src': fields.String(description='abosolute path to source file', required=True),
    'access_key': fields.String(description='AWS access key', required=False),
    'secret_key': fields.String(description='AWS secret key', required=False)
})

s3_existing_object = api.model('s3_existing_object', {
    'src': fields.String(description='path to source file', required=True),
    'access_key': fields.String(description='AWS access key', required=False),
    'secret_key': fields.String(description='AWS secret key', required=False)
})

aws_credentials = api.model('aws_credentials', {
    'access_key': fields.String(description='AWS access key', required=False),
    'secret_key': fields.String(description='AWS secret key', required=False)
})


@ns.route('/buckets')
class Buckets(Resource):
    """Lets you create a bucket"""
    @ns.doc('create bucket')
    @ns.expect(bucket)
    def post(self):
        """Create a new bucket"""
        s3_bucket = Bucket()
        return s3_bucket.create(api.payload)


@ns.route('/bucket/<string:bucket_name>/objects')
class Objects(Resource):
    """Lets you Add new objects(files) to S3 bucket"""
    @ns.doc('Add an object to bucket')
    @ns.expect(s3_new_object)
    def post(self, bucket_name):
        """Add an object to bucket"""
        s3_bucket = Bucket(bucket_name)
        return s3_bucket.add_object(api.payload)


@ns.route('/bucket/<string:bucket_name>/object/<string:key>')
class Object(Resource):
    """Lets you update delete objects from S3 bucket"""
    @ns.doc('Update an existing object')
    @ns.expect(s3_existing_object)
    def put(self, bucket_name, key):
        """Update an object"""
        s3_bucket = Bucket(bucket_name)
        return s3_bucket.update_object(key, api.payload)

    @ns.doc('Delete object from bucket')
    @ns.expect(aws_credentials)
    @ns.response(204, 'Object deleted')
    def delete(self, bucket_name, key):
        """Delete an object"""
        s3_bucket = Bucket(bucket_name)
        return s3_bucket.delete_object(key, api.payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
