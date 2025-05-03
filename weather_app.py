import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        print(f"Weather in {city}: {weather}, {temp}°C")
    else:
        print("City not found or error in fetching data.")

if __name__ == "__main__":
    city_input = input("Enter city name: ")
    get_weather(city_input)