import os 


input("Before proceeding make sure your Flask app is running on 'localhost:500' : ")
print("Press enter in all options for default settings")
#os.system("ssh-keygen")
os.system("ssh -R 80:localhost:5000 localhost.run")
print("Your Flask Application is visible over internet on the link given above.")