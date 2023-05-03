import boto3
import requests

def lambda_handler(event, context):
    url = "http://a15a0f4611ea24724ad4ea08e628f4e2-815442297.ap-south-1.elb.amazonaws.com/"
    try:
        response = requests.get(url)
        html_body = response.content.decode('utf-8')
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error retrieving HTML body from EKS: {e}'
        }

    # Return the complete HTML page as the response body
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': html_body
    }