import requests
import os
path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'media')
response=requests.get("https://www.javatpoint.com/fullformpages/images/mbps-full-form.jpg")
file=open(os.path.join(path,'mbps-full-form.jpg'),"wb")
file.write(response.content)
file.close()