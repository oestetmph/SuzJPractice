import requests


def weather_info():
    city = input('Please enter a city: ')
    state = input('Please enter a state: ')

    base_weather_api_url = 'http://api.openweathermap.org/data/2.5/weather?q='
    weather_api_url_key = '&appid=fc623e7c1bc984adfa3864bb04c2fc46'

    full_api_url = base_weather_api_url + str(city) + ',' + str(state) + weather_api_url_key

    raw_request = requests.get(full_api_url)
    raw_data = raw_request.json()

    city_name = raw_data['name']
    city_coordinates = raw_data['coord']
    raw_city_weather = raw_data['weather']
    city_weather = raw_city_weather[0]

    print('\n--' + str(city_name) + ' Coordinates--')
    print('Longitude: ' + str(city_coordinates['lon']))
    print('Latitude: ' + str(city_coordinates['lat']))

    print('\n--' + str(city_name) + ' Weather--')
    print(city_weather['description'])
