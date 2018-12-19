import requests
import urllib

Eng_language = {'nTqu':'','lang':'en'}
Ru_language = {'nTqM':'','lang':'ru'}
url_with_weather = 'http://wttr.in/{}'
list_with_location = ['London', 'SVO']

for location in list_with_location:
    print((requests.get(url_with_weather.format(location), params = Eng_language)).text)
print(requests.get(url_with_weather.format('Череповец'), params = Ru_language).text)  