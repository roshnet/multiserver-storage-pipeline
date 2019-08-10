import os
import requests

ENDPOINT = 'http://localhost:6000/storage'

""" Send a request to broker to save file on it """

FILENAME = 'soldier.jpg'

with open(FILENAME, 'rb') as fp:
    content = fp.read()

upload_resp = requests.post(os.path.join(ENDPOINT, FILENAME),
                            data=content)

print(upload_resp.text)
