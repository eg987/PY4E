# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

count = int(input('Enter count: '))
ct=int(count)
position= input('Enter position: ')
pn = int(position)

#get links
while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    lst=list()
    for tag in tags:
        lst.append(tag.get('href', None))  # Appends all the links to lst
    url = lst[pn-1] #might need -1 later
    count = count - 1
    print("Retrieving:", url)
    
