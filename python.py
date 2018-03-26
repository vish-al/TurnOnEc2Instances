import boto3
# Enter the region your instances are in, e.g. 'us-east-1'
region = 'ap-southeast-1'
# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']
instances = []

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    response= ec2.describe_instances(Filters=[
        {
		'Name': 'tag:Environment',
		'Values': ['QA']
		}])
    for r in response['Reservations']:
     for i in r['Instances']:
        instances.append(i['InstanceId'])
    #Uncomment below line to start instances
    #ec2.start_instances(InstanceIds=instances)
  
    
