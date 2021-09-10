import boto3
    
def lambda_handler(event, context):
    url = boto3.client('s3').generate_presigned_post(
        'YOUR_BUCKET',
        'test.txt',
        ExpiresIn=3600
    )
    
    return url
