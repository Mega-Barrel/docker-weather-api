#TODO
# Schedule every 30 min cron
# Dump data into DB

'''App to get weather API data.'''
import os
import requests
from dotenv import load_dotenv
from datetime import datetime

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
    API_URL = f'http://api.weatherapi.com/v1/current.json?key={key}&q={query}&dt={dt}'
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
    last_updated = resp['current']['last_updated']
    request_time = resp['location']['localtime']

    temp_c = resp['current']['temp_c']
    temp_f = resp['current']['temp_f']
    condition = resp['current']['condition']['text']
    
    wind_speed_kph = resp['current']['wind_kph']
    wind_speed_mph = resp['current']['wind_mph']
    
    feelslike_c = resp['current']['feelslike_c']
    feelslike_f = resp['current']['feelslike_f']

    return {
        'location': city_location,
        'last_updated': last_updated,
        'requested_time': request_time,
        'temp_c': temp_c,
        'temp_f': temp_f,
        'weather_condition': condition,
        'wind_speed_kph': wind_speed_kph,
        'wind_speed_mph': wind_speed_mph,
        'feelslike_c': feelslike_c,
        'feelslike_f': feelslike_f
    }

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
    curr_dt = datetime.now().strftime('%Y-%m-%d')

    # Fetch weather data
    resp = get_weather_data(API_KEY, QUERY, curr_dt)
    print(resp)

if __name__ == '__main__':
    main()
