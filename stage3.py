
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
load_dotenv()
import os



import glob
class AWSOps():
    def __init__(self,user_name=None,user_id=None,project_id=None,root_bucket='steeleyedata',region_name='ap-south-1')->None:
        '''Initialisation of all required vars'''
        ACCESS_KEY = str(os.environ.get('AWS_ACCESS_KEY'))
        SECRET_KEY = str(os.environ.get('AWS_SECRET_KEY'))  
        region_name = region_name
        self.s3_client = boto3.client('s3',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY,region_name=region_name)
        session = boto3.Session(aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
        self.resource = session.resource('s3')
        self.user_id = user_id
        self.user_name=user_name
        self.project_id = project_id
        self.root_bucket = root_bucket
        
    def get_bucket(self,bucket_name=None):
        bucket = self.resource.Bucket(self.root_bucket)
        return bucket

    def upload_bucket(self,file_name,bucket_name=None):
        self.s3_client.upload_file(
    Filename=file_name,
    Bucket=self.root_bucket,
    Key="steel.csv",
)
 