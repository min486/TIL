import requests
import time

base_url = 'http://localhost:8000/posts/'

for i in range(1, 100):
  requests.get(base_url + 'delete/' + str(i))