from utils.runner import run_playbook

playbooks = {
    'put': 'put_object.yml',
    'delete': 'delete_object.yml'
}


class S3object(object):
    """
    Class representing S3 object
    """
    def __init__(self, key=None):
        self._key = key

    def add(self, attributes):
        """
        Add object to S3 bucket
        :param attributes: API request payload
        :return: response - A tuple of message and return code
        """
        result = run_playbook(playbooks['put'], attributes)
        response = ('object uploaded', 201) if result[1] == 0 else ('failed to upload object, %s' %result[0], 400)
        return response

    def update(self, attributes):
        """
        Update an object in S3 bucket
        :param attributes: API request payload
        :return: response - A tuple of message and return code
        """
        attributes['key'] = self._key
        result = run_playbook(playbooks['put'], attributes)
        response = ('object updated', 200) if result[1] == 0 else ('failed to update object, %s' %result[0], 400)
        return response

    def delete(self, attributes):
        """
        Delete an object from S3 bucket
        :param attributes: API request payload
        :return: response - A tuple of message and return code
        """
        attributes['key'] = self._key
        result = run_playbook(playbooks['delete'], attributes)
        response = ('object deleted', 204) if result[1] == 0 else ('failed to delete object, %s' % result[0], 400)
        return response
