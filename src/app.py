import json

import boto3

ses = boto3.client('ses')

def lambda_handler(event, context):
    sender_email = 'alabioluwaseun40@gmail.com'  
    message_subject = 'Got your message by SNS?'
    # message_body = 'Hi there, this is an automated message delivered by SES, built upon SMTP'

    ses.send_email(
        Source=sender_email,
        Destination={
            'ToAddresses': [
               event['destinationEmail'],
            ]
        },
        Message={
            'Subject': {
                'Data': message_subject
            },
            'Body': {
                'Text': {
                    'Data': event['message']
                }
            }
        }
    )
    return 'Email sent!'