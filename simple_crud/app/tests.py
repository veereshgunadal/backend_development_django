from django.test import TestCase

# Create your tests here.
import requests
import json

url = 'http://127.0.0.1:8000'
post_data = {'roll':2, 'name': 'b', 'branch': 'y'}

get = requests.get(url+'/get')
print('get response :')
print(get.status_code)
print(get.json())


post = requests.post(url+'/post/', data = json.dumps(post_data))
print('post response :')
print(post.status_code)
print(post.json())

delete = requests.delete(url+'/delete/')
print('delete response :')
print(delete.status_code)
print(delete.json())