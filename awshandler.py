import logging
import boto3
from botocore.exceptions import ClientError
from progresspercentage import ProgressPercentage

class AWShandler():

    def __init__(self):
        self.region_name = 'us-east-1'
        self.aws_access_key_id = 'XXX'  #   Fill with yours
        self.aws_secret_access_key = 'XXX'  #    Fill with yours

    ## Please see -> https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
    def upload_file(self,file_name, bucket, object_name=None):
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name

        # Upload the file
        s3_client = boto3.client('s3',region_name=self.region_name,aws_access_key_id=self.aws_access_key_id,aws_secret_access_key=self.aws_secret_access_key)
        try:
            response = s3_client.upload_file(file_name, bucket, object_name, Callback=ProgressPercentage(f'{file_name}'))
        except ClientError as e:
            logging.error(e)
            return False
        return True
