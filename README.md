# docker-weather-api

Implementing a weather service to get the live *(every 10 minutes)* weather data for Mumbai city.

#### Notes
- This a ETL project which consumes weather api data and stores the data to a PostgreSQL databasea.
- Uses cronjob to execute the app/main.py script every 10 minutes.

## Weather API Token
Head over to [weatherapi](https://www.weatherapi.com/) site, and create a free account, and copy & paste API Key inside .env file

## .env file
Create a **.env** file inside the folder
Now open the **.env** file, add the following <u>without</u> any **''**, and save and close the file
```text
weather_api = enter your key
POSTGRES_HOST = host name
POSTGRES_PORT = port number
POSTGRES_DB = database name
POSTGRES_USER = database user
POSTGRES_PASSWORD = database password
```

## Setup - Requirements
  - Docker

## Setup - Docker Compose
### Environment Variable Setup
- Download or clone the repository.
- Create a .env file and add your credentials, as listed above.

## Run the Weather ETL Project
Run the container in either using detached mode
```bash
# Not using detached mode
docker compose up

# using detached mode
docker compose up -d
```

start/stop the docker containers
```bash
# start the container
docker container start

# stop the container
docker container stop
```

Stop and remove the containers (Optional). Note this will only remove the containers, not the database volumen and its base images.
```bash
docker compose down
```

The Weather API should now be executing and will display the output in the terminal.
Feel free to contribute to this project or report any issues you encounter. Happy coding!
