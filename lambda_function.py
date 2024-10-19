import json
import boto3
import requests

# List of your websites
# websites = [
#     'https://facebook.com',
#     'https://rajneete.com',
#     'https://bhive.ltd',
#     # Add more websites here...
# ]

websites = [
    'https://baahstore.com',
    'https://beta.baahstore.com',
    'https://bdgen24.com',
    'https://adminnews90.bdnextgen.com',
    'https://bdnextgen.com',
    'https://beta.bhive.ltd',
    'https://betabl.bhive.ltd',
    'https://bhive.ltd',
    'https://bladmin.bhive.ltd',
    'https://multi.bhive.ltd',
    'https://beta.deshmafood.com',
    'https://deshmafood.com',
    'https://funfurti.com',
    'https://atlas.ideahubbd.com',
    'https://atlascms.ideahubbd.com',
    'https://bajp.ideahubbd.com',
    'https://bdgen24.ideahubbd.com',
    'https://ideahubbd.com',
    'https://beta.linstargroup.com',
    'https://rajneete.com',
    'https://stratagemhub.com',
    'https://beta.swadeshionline.shop',
]


# SNS configuration
SNS_TOPIC_ARN = 'arn:aws:sns:us-west-1:067939645276:WebsiteStatusAlerts'  # Replace with your SNS Topic ARN

def notify_status(down_sites):
    sns_client = boto3.client('sns')
    subject = 'Website Status Alert'
    message = f'The following websites are down:\n' + '\n'.join(down_sites)
    sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=subject,
        Message=message
    )

def check_website_status():
    down_sites = []
    for site in websites:
        try:
           # response = requests.get(site)
            response = requests.get(site, timeout=30)  # Set a timeout of 10 seconds
            #if response.status_code != 200:
            if response.status_code not in (200, 301, 302):
                down_sites.append(site)
        except requests.exceptions.RequestException:
            down_sites.append(site)

    return down_sites

def lambda_handler(event, context):
    down_sites = check_website_status()
    if down_sites:
        notify_status(down_sites)
        return {
            'statusCode': 200,
            'body': json.dumps(f'Notification sent! Websites down: {down_sites}')
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('All websites are up.')
        }
