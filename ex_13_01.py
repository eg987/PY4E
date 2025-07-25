'''
Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/xml3.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = http://py4e-data.dr-chuck.net/comments_42.xml
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

stuff = uh.read()
stst = ET.fromstring(stuff)
lst = stst.findall('comments/comment')
lst2 = list()
for item in lst:
    lobj = item.find('count').text
    num = int(lobj)
    lst2.append(num)
tot = sum(lst2)
print(tot)
