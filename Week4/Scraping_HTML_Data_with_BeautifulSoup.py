# Week 4 - Assignment 1
# Can enter two links - http://py4e-data.dr-chuck.net/comments_42.html or http://py4e-data.dr-chuck.net/comments_869368.html

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Enter either of the URLs and read from them
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# If you print soup, each row looks like: <tr><td>Altyiab</td><td><span class="comments">99</span></td></tr>.
# We must now extract the span tags from here.

# Retrieve all of the span tags
tags = soup('span')

count = 0
int_list = []

for tag in tags:
    # print(tag) - if you print tag, you'll see: <span class="comments">99</span>.
    # We now must extract the contents of the tag (string) and convert it to int for summing.
    
    count += 1
    int_list.append(int(tag.contents[0]))

print("Count",count)
print("Sum",sum(int_list))
