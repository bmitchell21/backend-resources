# backend-resources
These files are what I used to create the backend resources for my version of the cloud resume challenge.

Please note that updates will be required if you want to use these files as your own.

In the buildspec.yml file you will need to update the bucket name on lines 10 and 11. If you don't yet have a designated bucket, create one. If you have installed the AWS CLI, use the command below to create a bucket.

aws s3 mb s3:// your-bucket-name-here

You will also need to remove lines 12 - 15 until you have your API url. 

Once you deploy the resources and have your API url, update line 11 of the test_handler.py file accordingly. Add the post_build commands back to the buildspec.yml file.

Please reach out with any questions.