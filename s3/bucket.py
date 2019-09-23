from utils.runner import run_playbook
from s3.s3_object import S3object

playbooks = {
    'create': 'create_bucket.yml'
}


class Bucket(object):
    """
    Class representing AWS S3 bucket
    """
    def __init__(self, name=None):
        self._name = name

    def create(self, attributes):
        """
        Create S3 bucket
        :param attributes: API request payload
        :return: response - A tuple of message and return code
        """
        result = run_playbook(playbooks['create'], attributes)
        response = ('bucket created', 201) if result[1] == 0 else ('failed to create bucket, %s' %result[0], 400)
        return response

    def add_object(self, attributes):
        """
        Add an object to bucket
        :param attributes: API request payload
        :return: response - A tuple of message and return code
        """
        attributes['bucket_name'] = self._name
        s3_object = S3object()
        return s3_object.add(attributes)

    def update_object(self, key, attributes):
        """
        Update an existing object in bucket
        :param key: keyname of the S3 object
        :param attributes: API request payload
        :return: response - A tuple of message and return code
        """
        attributes['bucket_name'] = self._name
        s3_object = S3object(key)
        return s3_object.update(attributes)

    def delete_object(self, key, attributes):
        """
        Delete an existing object in bucket
        :param key: keyname of the S3 object
        :param attributes: API request payload
        :return: response - A tuple of message and return code
        """
        attributes['bucket_name'] = self._name
        s3_object = S3object(key)
        return s3_object.delete(attributes)
