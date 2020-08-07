# Week 6 - Assignment 1
# Links: http://py4e-data.dr-chuck.net/comments_42.json, http://py4e-data.dr-chuck.net/comments_869371.json

import urllib.request, urllib.parse, urllib.error
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print("Retrieving ", url)

connection = urllib.request.urlopen(url, context=ctx)
url_info   = connection.read().decode()
print("Retrieved ",len(url_info)," characters")

info = json.loads(url_info)
# print(json.dumps(info, indent=2))

count = 0
sum_  = 0
for item in info["comments"]:
    sum_  += int(item['count'])
    count += 1
    
print("Count: ", count)
print("Sum: ", sum_)
