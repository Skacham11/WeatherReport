import tkinter as tk
import secrets
import requests
from datetime import datetime
 



def getWeather(canvas):
    location = textField.get()
    api_key = secrets.user_api_key
    full_API_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    api_link_response = requests.get(full_API_link)
    api_data = api_link_response.json()
    country_name = api_data['sys']['country']
    temp_city_farenheit = ((api_data['main']['temp'] - 273.15) * 1.8 + 32)
    weather_description = api_data['weather'][0]['description']
    wind_speed = api_data['wind']['speed']
    pressure = api_data['main']['pressure']
    humidity = api_data['main']['humidity'] 

    final_info = str(round(temp_city_farenheit))  + " " + "°F" 
    final_data = "\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind_speed) + "\n" +"Weather Description: " + str(weather_description) + "\n" +"Country: " + str(country_name)
    final_data = "\n" + "Country: " + str(country_name) + "\n" +"Current date & time is: " + datetime.now().strftime("%d %b %y | %H:%M:%S") + "\n" + "Weather description: " + str(weather_description) + "\n" + "Wind speed: " + str(wind_speed) + "\n" +"Current humidity: " + str(humidity) + "\n" + "Pressure: " + str(pressure) 
    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.configure(background='lime green')


canvas.title("Weather App",)
f = ("Roboto", 20, "bold")
t = ("Roboto", 40, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()

button = tk.Button(canvas, text = "Get Weather", font = f, command = lambda: getWeather(canvas)).pack(pady = 50)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()


canvas.mainloop()




