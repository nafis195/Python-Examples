# Bismillahir Rahmanir Rahim


import requests
import os
import webbrowser as wb


url = "http://dimikcomputing.com"
responses = requests.get(url)

with open ("test23_dimik.html", "w", encoding=responses.encoding) as f:
    f.write(responses.text)

file_path = os.path.realpath("test23_dimik.html")
print(file_path)

wb.open("file://" + file_path)