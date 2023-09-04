# docker-weather-api

Implementing a weather service for getting current weather, and previous day weather for Mumbai city using Weather API

## Setup - code
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

## Setup - Docker
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
The Weather API should now be executing and will display the answer in terminal.

Feel free to contribute to this project or report any issues you encounter. Happy coding!