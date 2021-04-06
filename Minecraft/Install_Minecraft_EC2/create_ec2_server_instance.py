import boto3


ec2 = boto3.resource('ec2', region_name='us-east-1')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-013f17f36f8b1fefb',
     MinCount=1,
     MaxCount=1,
     InstanceType='c4.large',
     KeyName='SpinningOps_Key',

     SecurityGroupIds=[
        'sg-0ca648b5cfead1029',
    ],

     InstanceMarketOptions={
         'MarketType': 'spot',
         'SpotOptions': {
             'MaxPrice': '0.0785',
             'SpotInstanceType': 'one-time',
             'InstanceInterruptionBehavior': 'terminate'
        },
    }
)