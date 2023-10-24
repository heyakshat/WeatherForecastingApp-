import tkinter as tk
import requests

# OpenWeatherMap API key (replace with your own)
api_key = '9ab48782b954e117ae00f8d4144c491e' 

def get_weather(city):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        weather_desc = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        result_text.set(f'Weather: {weather_desc}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s')
    except Exception as e:
        result_text.set('Error fetching data')

def search_weather():
    city = city_entry.get()
    get_weather(city)

# Create the GUI window
window = tk.Tk()
window.title("Weather Forecast App")

# Label
city_label = tk.Label(window, text="Enter City:")
city_label.pack(pady=10)

# Entry for city input
city_entry = tk.Entry(window)
city_entry.pack(pady=5)

# Button to search for weather
search_button = tk.Button(window, text="Search Weather", command=search_weather)
search_button.pack(pady=10)

# Display weather results
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text)
result_label.pack(pady=10)

window.mainloop()
