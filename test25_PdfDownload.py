# Bismillahir Rahmanir Rahim


import requests
import sys


base_url = "http://subeen.com/download"
info = {"Name": "Subeen", "Email": "book@subeen.com", "Country": "BD"}
url = base_url + "process.php"
responses = requests.post(url, data=info)

if responses.ok is False:
    sys.exit("Error downloading the file")

with open("test25_cpbook.pdf", "wb") as myBook:
    myBook.write(responses.content)

print("Book download successful!")