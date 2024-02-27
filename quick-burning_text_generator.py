import os
import sys
import requests
from PIL import Image
import io
import pyperclip
import subprocess
import time

url = "https://cooltext.com/PostChange"

headers = {
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8"
}
text = input("Input text: ")
data = {
    'LogoID': "4",
    'Text': text,
    'FontSize': 70,
    'Color1_color': "#FF0000", #Text color
    'Integer1': 15, #Flame Angle
    'Boolean1': "on",
    'Integer9': 0,
    'Integer13': "on",
    'Integer12': "on",
    'BackgroundColor_color': "#FFFFFF"
}

response = requests.post(url, headers=headers, data=data)

if response.status_code != 200:
    print("Request failed")
    print("Error: " + response.text)
    sys.exit()

image_url = response.json()['renderLocation']
response = requests.get(image_url, verify=False)

if response.status_code != 200:
    print("Request failed")
    print("Error: " + response.text)
    sys.exit()

image = Image.open(io.BytesIO(response.content))
file_path = os.path.dirname(os.path.abspath(__file__)) + "/temp_image.gif"
with open(file_path, "wb") as image_file:
    image_file.write(response.content)

subprocess.Popen(['xdg-open', file_path])
time.sleep(5)
os.remove(file_path)