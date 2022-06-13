import secrets
import requests
from datetime import datetime

 

api_key = secrets.user_api_key

location = input('Enter location: ')
print("\n")
print('Retrieving data for', location)
print("----------------------------------------------------------------------")

print("\n")

full_API_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

api_link_response = requests.get(full_API_link)

api_data = api_link_response.json()



if api_data['cod'] == '404':
    print("City is not found: {}, Please check City name".format(location))

else:
    temp_city_farenheit = ((api_data['main']['temp'] - 273.15) * 1.8 + 32)
    weather_description = api_data['weather'][0]['description']
    wind_speed = api_data['wind']['speed']
    country_name = api_data['sys']['country']
    print("Country: {}".format(country_name))
    print("Current date & time is: " + datetime.now().strftime("%d %b %y | %H:%M:%S"))
    print("Current temperature in {} is {} F".format(location, temp_city_farenheit))
    print("Weather description: {}".format(weather_description))
    print("\n")
    print("Wind speed: {}".format(wind_speed))
    print("Current humidity: {}".format(api_data['main']['humidity']))


