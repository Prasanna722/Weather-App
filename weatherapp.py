import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "fcfba0fa23a3fdd65b4af91fa9f3fc82"  # Replace with your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(base_url)
        data = response.json()
        
        if response.status_code == 200:  # Successful response
            if 'main' in data:  # Check if 'main' key exists
                main_data = data["main"]
                temperature = main_data["temp"]
                pressure = main_data["pressure"]
                humidity = main_data["humidity"]
                
                weather_description = data["weather"][0]["description"]
                wind_speed = data["wind"]["speed"]
                
                # Update the result labels
                result_label.config(text=f"Temperature: {temperature}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nWeather: {weather_description}\nWind Speed: {wind_speed} m/s")
            else:
                result_label.config(text="Could not retrieve weather data.")
        else:
            result_label.config(text="City not found. Please check the city name.")
        
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error: {e}")

# Tkinter GUI
root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter city name:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_button = tk.Button(root, text="Get Weather", command=get_weather)
get_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
