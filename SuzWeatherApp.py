import requests

city = input('Please enter in your city ')
state = input('Please enter in your state ')

base_weather_api = 'http://api.openweathermap.org/data/2.5/weather?q='
weather_api_url_key = '&appid=fc623e7c1bc984adfa3864bb04c2fc46'

full_api_url = base_weather_api + str(city) + ',' + str(state) + weather_api_url_key

weather_request = requests.get(full_api_url)
weather_request_data = weather_request.json()

city_name = weather_request_data['name']
city_coord = weather_request_data['coord']
raw_city_weather = weather_request_data['weather']
city_weather = raw_city_weather[0]

# diberiville_weather = weather_request_data['weather']
# diberiville_coord = weather_request_data['coord']

# print('The coordinates of Diberiville are : ' + str(diberiville_coord))
# print('The weather of Diberciville is : ' + str(diberiville_weather))

print('\n\n-- ' + str(city_name) + ' Coordinates--')
print('Longitude: ' + str(city_coord ['lon']))
print('Latitude: ' + str(city_coord ['lat']))

print('\n\n-- ' + str(city_name) + ' Weather--')
print(city_weather['description'])
