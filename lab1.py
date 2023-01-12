import requests 

r = requests.get("http://www.google.com/")    
k = requests.get("https://raw.githubusercontent.com/avj99/CMPUT404-lab01/master/lab1.py")
# print(requests.__version__)
# print(r.text)   
print(k.text)
