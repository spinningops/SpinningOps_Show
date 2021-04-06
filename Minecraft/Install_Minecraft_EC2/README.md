# How to install Minecraft ec2 server

1. Create virtualenv   
`virtualenv .venv`   
2. Activate env
`source .venv/bin/activate`   
3. Install boto3   
`pip3 install boto3`   
4. Create ec2 instance   
5. set executable and run ` sh install_docker.sh`   
6. Start the Minecraft server   
`docker run -d -p 25565:25565 --name mc -e EULA=TRUE itzg/minecraft-server`   
7. Start the Minecraft Client   
`python3 create_ec2_client_instance.py`   
8. Play


