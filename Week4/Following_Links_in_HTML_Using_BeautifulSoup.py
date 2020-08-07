# Week 4 Assignment 2
# Following Links in Python- http://py4e-data.dr-chuck.net/known_by_Fikret.html, http://py4e-data.dr-chuck.net/known_by_Gracealexandra.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url   = input('Enter: ')
count = input('Enter count: ')
pos   = input('Enter position: ')

name_list = []

for i in range(int(count)+1):
    print("Retrieving: ", url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags   = soup('a')
    url_a  = tags[int(pos)-1]
    url    = url_a.get('href', None)
