import boto3
import os

ses = boto3.client('ses')

def send_email(to_address, subject, body):
    response = ses.send_email(
        Source=os.environ['source@example.com'],
        Destination={
            'ToAddresses': [to_address],
        },
        Message={
            'Subject': {
                'Data': subject,
            },
            'Body': {
                'Text': {
                    'Data': body,
                },
            },
        }
    )
    return response

def lambda_handler(event, context):
    recipient_list = [
        'recipient1@example.com',
        'recipient2@example.com',
    ]
    
    subject = "Your Subject Here"
    body = "Your email body here"

    for recipient in recipient_list:
        response = send_email(recipient, subject, body)
        print(f"Email sent to {recipient}: {response}")
        
    return {
        'statusCode': 200,
        'body': 'Emails sent successfully'
    }
