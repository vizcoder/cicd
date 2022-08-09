import os
import boto3
from botocore.client import Config
import os
from urllib.parse import urlparse
import tarfile

# New Numee Ai AWS Server
ACCESS_KEY = 'AKIA4PZIBH7I7Z5P4BEZ'
SECRET_KEY = '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'
BUCKET = 'numee-ai'
VIDEOS_CACHE_FOLDER = 'Ai/Cache'
REGION = 'ap-south-1'

s3_resource = boto3.resource(
    's3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                         aws_secret_access_key=SECRET_KEY)


def get_bucket_file(s3_uri):
    u = urlparse(s3_uri, allow_fragments=False)
    bucket = u.netloc
    file_path = u.path.lstrip('/')
    return bucket, file_path


def download_from_s3(bucket_name, key, model_folder, object_key=None):
    if object_key is None:
        object_key = os.path.join(model_folder, os.path.split(key)[1])
    else:
        object_key = object_key+'_'+os.path.split(key)[1]
    if os.path.exists(object_key):
        return object_key
    else:
        try:
            s3_resource.Bucket(
                bucket_name).download_file(key, object_key)
        except Exception as e:
            raise Exception(
                'The file {} is not available\n{}'.format(key, str(e)))
        return object_key


def unzip_model(source, destination):

    # open file
    file = tarfile.open(source)

    # print file names
    print(file.getnames())

    # extract files
    file.extractall(destination)

    # close file
    file.close()
