# added import at the top, this compiles
import requests

r = requests.get('https://api.github.com/users/Connor-SM')

print(r)
print(type(r))

#accessing the content that we requested from the URL

data = r.content
print(data)


# converting data from JSON into a python dictionary and outputting all key-value pairs

data = r.json()

for k, v in data.items():
    print(f'Key:{k}\t Value: {v}')
    
print('Accessing Data Directly')
print(data['name'])


#outputting specific value pairs 

r = requests.get('https://api.github.com/search/repositories?q=language:python')
data = r.json()
print(data["total_count"])


#DIY EXERCISES: 1) Java Script Reposittoriews.Using the requests module and the Github API lonl in our lesspn, figue abput repositories on Github use JavaScript

r = requests.get('https://api.github.com/search/repositories?q=language:javascript')
data = r.json()
print(data["total_count"])
