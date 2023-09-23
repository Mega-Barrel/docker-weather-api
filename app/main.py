'''App to get weather API data.'''

import os
import pytz
import psycopg2
import requests
from datetime import datetime
from dotenv import load_dotenv
from time import ( strftime, localtime )

class WeatherApi():
    
    def __init__(self):
        """
        Constructor
        """
        load_dotenv()
        
        # Constants
        self.api_key = self.get_api_key()
        self.query = 'Mumbai'
        # Get previous day's date
        self.curr_dt = datetime.now().strftime('%Y-%m-%d')

        self._db_params = {
            "host": "postgres",
            "database": "weather-api-db",
            "user": "saurabh",
            "password": "test-weather-api"
        }

    def get_api_key(self):
        """
        Returns the API key from environment variable.
        """
        API_KEY = os.environ.get('weather-api')
        if not API_KEY:
            raise ValueError('API key is not available.')
        else:
            return API_KEY

    # Extract
    def request_data(self, key, query, dt):
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

    # Transform
    def get_weather_data(self, resp):
        """
        Retrieve weather data for a given location and date.
        """
        def convert_time_gmt_to_ist(epoch_time):
            formatted_time = strftime('%Y-%m-%d %H:%M:%S', localtime(epoch_time))
            # Define the GMT timezone
            gmt_timezone = pytz.timezone('GMT')
            # Create a datetime object from the formatted time
            gmt_datetime = datetime.strptime(formatted_time, '%Y-%m-%d %H:%M:%S')
            # Set the timezone to IST
            ist_timezone = pytz.timezone('Asia/Kolkata')
            ist_datetime = gmt_timezone.localize(gmt_datetime).astimezone(ist_timezone)
            # Format the IST datetime as a string
            formatted_ist_time = ist_datetime.strftime('%Y-%m-%d %H:%M:%S')
            return formatted_ist_time
        
        country = resp['location']['country']
        city = resp['location']['name']

        # convert the epoch time to datetime format
        last_updated = convert_time_gmt_to_ist(resp['current']['last_updated_epoch'])
        request_time = convert_time_gmt_to_ist(resp['location']['localtime_epoch'])

        temp_c = resp['current']['temp_c']
        temp_f = resp['current']['temp_f']
        condition = resp['current']['condition']['text']
        
        wind_speed_kph = resp['current']['wind_kph']
        wind_speed_mph = resp['current']['wind_mph']
        
        feelslike_c = resp['current']['feelslike_c']
        feelslike_f = resp['current']['feelslike_f']

        # Return JSON Object
        return {
            'country': country,
            'city': city,
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

    def load_record(self, data):
        """
        Method to Insert weather data to PostgreSQL DB
        
        :param data
            JSON Object
        """
        try:
            # Create a connection to the PostgreSQL database
            connection = psycopg2.connect(**self._db_params)

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            #  Query
            query = """
                INSERT INTO weather_data (
                    country, city, last_updated,
                    requested_time, temp_c, temp_f,
                    weather_condition, wind_speed_kph, wind_speed_mph,
                    feelslike_c, feelslike_f
                ) VALUES (
                    %s, %s, %s,
                    %s, %s, %s,
                    %s, %s, %s,
                    %s, %s
                )
            """
            values = (
                data['country'], data['city'], data['last_updated'],
                data['requested_time'], data['temp_c'], data['temp_f'],
                data['weather_condition'], data['wind_speed_kph'], data['wind_speed_mph'],
                data['feelslike_c'], data['feelslike_f']
            )

            # Execute SQL queries here
            cursor.execute(query, values)
            # commit changes and close the cursor and connection
            connection.commit()
            cursor.close()
            connection.close()
            print('Inserted weather record')

        except psycopg2.Error as e:
            print("Error connecting to PostgreSQL:", e)

    def etl_report(self):
        """
        Method to execute ETL process
        """
        # Extract
        resp = self.request_data(key=self.api_key, query=self.query, dt=self.curr_dt)
        # Transform
        data = self.get_weather_data(resp=resp)
        # Load
        self.load_record(data=data)


def main():
    """
    Method to create WeatherApi object and execute the process
    """
    weather_api = WeatherApi()
    weather_api.etl_report()

if __name__ == '__main__':
    main()
