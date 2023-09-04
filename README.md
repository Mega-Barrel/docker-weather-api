# docker-weather-api

Implementing a weather service to get the previous day's weather data for Mumbai city using Weather API.

## .env file
Create a **.env** file inside the folder
Now open the **.env** file, add the following, and save and close the file
```text
weather-api = 'YOUR API Key'
```

## Weather API Token
Head over to [weatherapi](https://www.weatherapi.com/) site, and create a free account, and copy & paste API Key inside .env file

## Setup - local
To use the Weather API Tool, follow the steps below:

**1. Clone the repository:** git clone https://github.com/Mega-Barrel/docker-weather-api.git

**2. Navigate to the project directory:** cd docker-weather-api

**3. Set up a virtual environment (optional but recommended):**
- On Windows:
  ```
  python -m venv weather-api-env
  weather-api-env\Scripts\activate
  ```

- On Linux/macOS:
  ```
  python3 -m venv weather-api-env
  source weather-api-env/bin/activate
  ```
**4. Install the required dependencies:** pip install -r requirements.txt

Now you can run the Weather API locally.
```bash
python3 app/main.py
```

## Setup - Docker
### Environment Variable Setup
Open the Dockerfile, go to line 26, and paste your bearer token where it says **'API Key'**. Eg:
```Dockerfile
# SET ENVIRONMENT VARIABLE
ENV weather-api 'Paste your API Key'
```

### Build the Docker Image & Run the container
To run the Weather API using Docker, follow these steps:
  1.  Install Docker: [Docker Installation Guide](https://docs.docker.com/get-docker/)
  2. Build the Docker image: 
  ```bash
   docker build -t weather-api .
  ```
  3. Run the Docker container:
  ```bash
   docker run --rm weather-api .
  ```
The Weather API should now be executing and will display the output in the terminal.

Feel free to contribute to this project or report any issues you encounter. Happy coding!
