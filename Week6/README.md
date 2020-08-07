## Assignment 1 - Extracting Data from JSON

The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file.  
1. [http://py4e-data.dr-chuck.net/comments_42.json](http://py4e-data.dr-chuck.net/comments_42.json) (Sum=2553)
2. [http://py4e-data.dr-chuck.net/comments_869371.json](http://py4e-data.dr-chuck.net/comments_869371.json)

## Assignment 2 - Using the GeoJSON API

The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.  
To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:  
[http://py4e-data.dr-chuck.net/json?](http://py4e-data.dr-chuck.net/json?)  
This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response. To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function.  

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJy0Uc1Zmym4gR3fmAYmWNuac".
