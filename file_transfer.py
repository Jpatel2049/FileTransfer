# Gets the username from the Credentials text file
def get_username():
    with open("Credentials.json") as file:
        data = json.load(file)
        return data['Username']


# Gets the password form Credentials text file
def get_password():
    with open("Credentials.json") as file:
        data = json.load(file)
        return data['Password']


import paramiko
import json
from datetime import datetime

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Assigns the username and password to variables 
my_user = get_username()
my_password = get_password()

ssh.connect(hostname='3.90.221.119',username=my_user,password=my_password, port=22)

stfp_clinet = ssh.open_sftp()

# Putting the FILE X & FILE Y onto the remote server
stfp_clinet.put('File x.txt', "/home/EC2/File x.txt")
stfp_clinet.put('File y.txt', "/home/EC2/File y.txt")

# Downloads a file from the remote server onto the local machine
stfp_clinet.get("/home/EC2/File", "/Users/jay/File Transfer/File")

stfp_clinet.close()
ssh.close()

dateTimeObj = datetime.now()
print("Files Trasnfer Complete at ", dateTimeObj)

