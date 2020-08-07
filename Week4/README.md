## Assignment 1: Scraping Numbers from HTML using BeautifulSoup

The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.  

You can enter 2 urls:
1. [http://py4e-data.dr-chuck.net/comments_42.html](http://py4e-data.dr-chuck.net/comments_42.html) (sum = 2553)
2. [http://py4e-data.dr-chuck.net/comments_869368.html](http://py4e-data.dr-chuck.net/comments_869368.html)


## Assignment 2: Following Links in HTML Using BeautifulSoup

The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.  

1. Start at [http://py4e-data.dr-chuck.net/known_by_Fikret.html](http://py4e-data.dr-chuck.net/known_by_Fikret.html)  
Find the link at position **3** (the first name is **1**). Follow that link. Repeat this process **4** times. The answer is the last name that you retrieve.  
**Sequence of names**: Fikret Montgomery Mhairade Butchi Anayah
**Last name in sequence**: Anayah  
2. Actual problem: Start at: [http://py4e-data.dr-chuck.net/known_by_Gracealexandra.html](http://py4e-data.dr-chuck.net/known_by_Gracealexandra.html)  
Find the link at position **18** (the first name is **1**). Follow that link. Repeat this process **7** times. The answer is the last name that you retrieve.
