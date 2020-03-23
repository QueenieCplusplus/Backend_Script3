import urllib.request
import json
import ssl
import googleapiclient

endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

ssl._create_default_https_context = ssl._create_unverified_context

# api_key = ''// shall have key from API

origin = input('where are you?: ').replace('','+')

destination = input('where do you want to go?: ').replace('','+')

mode = input('what kind of transportation tool you are using?:')

nav_request = 'origins={}&destinations={}&key={}'.format(origin, destination, api_key)

request = endpoint + nav_request

response = urllib.request.urlopen(request).read()   # url String

distances = json.loads(response) #

print(distances)