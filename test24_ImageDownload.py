# Bismillahir Rahmanir Rahim


import requests

img_url = "https://goo.gl/PsibBu"
image = requests.get(img_url)

with open ("test24_myImage.png", "wb") as myFile:
    myFile.write(image.content)