# Week 5 - Assignment
# Enter the links: http://py4e-data.dr-chuck.net/comments_42.xml, http://py4e-data.dr-chuck.net/comments_869370.xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

results = tree.findall('.//count')

count = 0
sum_  = 0
for res in results:
    sum_  = sum_ + int(res.text)
    count += 1

print("Count",count)
print("Sum",sum_)
