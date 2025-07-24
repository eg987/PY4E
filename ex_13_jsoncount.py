import urllib.request, urllib.parse, urllib.error
import json
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_42.json'

req = urllib.request.urlopen(url).read().decode('utf-8') #covert bytes into string using decode('utf-8')

char_count = len(req) #count characters using len() func

data = json.loads(req) #make json into python object


sum_list = []
for item in data['comments']:
    sum_list.append(item['count'])

print('Retrieving', url)
print('Retrieved', char_count, 'characters')
print('Numbers: ', sum_list)
print('Count:', len(sum_list))
print('Sum:', sum(sum_list))