from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '62c111d6d569b3037cbfbb9f5bb9b362'  # Replace with your actual OpenWeatherMap API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        country = request.form.get('country')

        if city:
            query = f"{city},{country}" if country else city

            params = {
                'q': query,
                'appid': API_KEY,
                'units': 'metric'
            }

            response = requests.get(BASE_URL, params=params)
            print("Request URL:", response.url, flush=True)

            try:
                data = response.json()
                print("API response:", data, flush=True)

                if response.status_code == 200:
                    weather_data = {
                        'city': data['name'],
                        'temperature': data['main']['temp'],
                        'description': data['weather'][0]['description'],
                        'icon': data['weather'][0]['icon']
                    }
                else:
                    weather_data = {'error': data.get('message', 'City not found')}
            except Exception as e:
                weather_data = {'error': f'Error parsing response: {e}'}
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
