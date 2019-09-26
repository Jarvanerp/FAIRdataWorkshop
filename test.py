
# importing the requests library 
import requests 

  
# api-endpoint 
URL = "http://localhost:8890/sparql/?default-graph-uri=http%3A%2F%2Fexample.com&query=select+*+where+%7B+%3Fs+%3Fp+%3Fo%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+"
  
    # extracting data in json format 
    # sending get request and saving the response as response object 
r = requests.get(url = URL) 
print(r.content)
data = r.json() 
print(data)