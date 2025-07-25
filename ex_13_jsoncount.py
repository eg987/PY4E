'''
Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to 
http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON 
data from that URL using urllib and then parse and extract the comment counts from the
JSON data, compute the sum of the numbers in the files and submit the sum as your answer:

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
'''

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
