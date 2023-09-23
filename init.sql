-- weather Table
CREATE TABLE weather_data (
    country VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    last_updated TIMESTAMP NOT NULL,
    requested_time TIMESTAMP NOT NULL,
    temp_c DECIMAL(5, 2) NOT NULL,
    temp_f DECIMAL(5, 2) NOT NULL,
    weather_condition VARCHAR(255) NOT NULL,
    wind_speed_kph DECIMAL(5, 2) NOT NULL,
    wind_speed_mph DECIMAL(5, 2) NOT NULL,
    feelslike_c DECIMAL(5, 2) NOT NULL,
    feelslike_f DECIMAL(5, 2) NOT NULL
);
