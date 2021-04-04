# Install Jenkins Container using Docker as a disposable resource

How to install Jenkins using Docker at AWS spot instance and add persistant data

Requirements: 
`virtualenv .venv`
`pip3 install boto3`
Activate venv
`source .venv/bin/activate`

1. create Jenkins instance
2. allocate elastic IP
3. create IAM user
4. create new IAM role EC2Full
5. attach IAM role to Jenkins
6. install docker
7. install ebs plugin
8. create ebs volume
9. build jenkins image
10. start jenkins container
11. configure jenkins


Install ebs plugin
`docker plugin install rexray/ebs EBS_ACCESSKEY=$AWSKEY EBS_SECRETKEY=$AWSSECRET`

Create ebs volume
`sudo docker volume create -d rexray/ebs jenkins_home --opt=size=10`

Start jenkins container
`sudo docker run -p 8080:8080 -p 5000:5000 --volume-driver=rexray/ebs -v jenkins_home:/var/jenkins_home jenkins:alpine`

Build jenkins image
`sudo docker build -t jenkins:alpine .`