'''App to get weather API data.'''
import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta

def get_api_key():
    """
    Returns the API key from environment variable.
    """
    API_KEY = os.environ.get('weather-api')
    if not API_KEY:
        raise ValueError('API key is not available.')
    else:
        return API_KEY

def request_data(key, query, dt):
    """
    Method to Make a call to weather API
    
    params:
        key: Weather API Key
        query: Search location
        dt: date

    returns:
        JSON object, else 'Err
    """
    API_URL = f'http://api.weatherapi.com/v1/history.json?key={key}&q={query}&dt={dt}'
    resp = requests.get(API_URL)
    
    if resp.status_code == 200:
        print('API Status ' + str(resp.status_code) + ' OK')
        return resp.json()
    else:
        return 'Error while retriving data'

def get_weather_data(api_key, query, date):
    """
    Retrieve weather data for a given location and date.
    """
    resp = request_data(key=api_key, query=query, dt=date)
    city_location = f"{resp['location']['name']}/{resp['location']['country']}"
    curr_hour = f"{resp['location']['localtime']}"
    weather = f"Weather: {resp['forecast']['forecastday'][0]['day']['avgtemp_c']}"
    weather_condition = f"{resp['forecast']['forecastday'][0]['day']['condition']['text']}"

    # print the weather status
    print(f"{city_location} {curr_hour} {weather} Celsius, {weather_condition}")

def main():
    """
    Method to call current_hour weather data,
    and previous day data.
    """
    load_dotenv()
    
    # Constants
    API_KEY = get_api_key()
    QUERY = 'Mumbai'

    # Get previous day's date
    curr_dt = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

    # Fetch weather data
    get_weather_data(API_KEY, QUERY, curr_dt)

if __name__ == '__main__':
    main()
