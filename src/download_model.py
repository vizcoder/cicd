
import os
import boto3
from botocore.client import Config
import os
from urllib.parse import urlparse
import shutil
import os

from download_model_utils import *


# model_file_uri = "s3://numee-ai/Ai/Models/Mark2_Swap_Numee_Prod.tar.gz"
# model_file_uri = "s3://numee-ai/Ai/Models/talkingHeads_Model.tar.gz"
# model_file_uri = "s3://numee-ai/Ai/Models/model1.tar.gz"
model_file_uri = "s3://numee-ai/Ai/Models/model2.tar.gz"

# prefix = "../localhost/Data_Folder/"
prefix = "/opt/ml/"

model_folder = os.path.join(prefix, 'model')
if not os.path.exists(model_folder):
    os.mkdir(model_folder)
    print('model Directory Created')


bucket, key = get_bucket_file(model_file_uri)
print(bucket, key)

model_zip_path = os.path.join(model_folder, os.path.split(key)[1])

# if the new model is not present then 
# remove the whole model directory and 
# download the new model from s3
# then unzip the new model into the model folder

if not os.path.exists(model_zip_path): 
    print("Model Changed.")

    # delete the old model directory
    model_folder_abspath = os.path.abspath(model_folder)
    shutil.rmtree(model_folder_abspath, ignore_errors=True)
    print("Deleting old model directory")
    
    # create model directory
    os.mkdir(model_folder)
    print("Model Directory created")
     
    # download the new model directory    
    model_zip_path= download_from_s3(bucket, key,model_folder)
    print("model_zip_path",model_zip_path)
    
    # unzip the new model into the model folder
    unzip_model(model_zip_path,model_folder)
    print("model unzipped successfully")

else:
    print("Model Not Changed. Using Old Model...")
    