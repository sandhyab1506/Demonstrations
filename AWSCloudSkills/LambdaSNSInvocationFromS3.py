import json
import boto3
import urllib

# boto3 is a python library to manage AWS services
s3_client = boto3.client('s3')
sns_client = boto3.client('sns')



def lambda_handler (event, context):
    
    # To retrieve the bucket name and the just uploaded file from the last event (which is the first one of the list 'Records')
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    key = urllib.parse.unquote_plus(key, encoding='utf-8')
    
    # To use get_object() function to retrieve content from the S3 bucket
    response = s3_client.get_object(Bucket=bucket_name,Key=key)
    contents = response["Body"].read().decode()
    
    # In this code we are trying to return the number of words in the uploaded file
    words = contents.split()
    message = 'The word count in the file ' + key + ' is '+ str(len(words))
    print(message)

    # This message will be printed in the CloudWatch logs
    print("those are the contents of the file : \n" , contents)
   
   
   # To associate the message to the SNS topic 
    sns_response = sns_client.publish(
        TargetArn='<The arn of the created SNS topic>',  # Copy it from your created SNS topic
        Message= str(message),             # This will be the body of your email
        Subject= str('Word Count Result')  # This will be the subject of your email
        )
