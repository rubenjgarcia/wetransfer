import boto3

def lambda_handler(event, context):
    url = boto3.client('s3').generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': "YOUR_BUCKET", 'Key': "test.txt"},
        ExpiresIn=3600,
    )
    return {"url": url}
