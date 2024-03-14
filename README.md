<h1>End to End MAchine Learning Project - AWS-CI-CD_Pipeline</h1>

1. Docker build check 

2. create github workflow file

3. create IAM user in aws and give necessary permissions.

4. create EC2 Instance and launch it.

5. create ECR Repository and copy its URL save in Notepad.

6. Now connect EC2 Instance and launch the Console for Docker setup and github action runner.

<h1>Docker Setup In EC2 commands to be Executed</h1>

sudo apt-get update -y

sudo apt-get upgrade

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

<h1>Configure EC2 as self-hosted runner:</h1>

create github action runner from repo settings.

select linux

copy all the commands in console for self hosted runner.

<h1>Setup github secrets:</h1>

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>> 566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app
