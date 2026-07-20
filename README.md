# Weather ETL Pipeline

A fully automated Python pipeline that extracts live weather data from the OpenWeatherMap API, transforms it, and loads it into a SQLite database. The pipeline runs daily at 8 AM via Windows Task Scheduler.

## Features

- **Extract**: Pulls current weather data for Gaborone, Botswana
- **Transform**: Parses JSON and extracts temperature, humidity, and weather description
- **Load**: Appends clean data to a SQLite database (`weather.db`)
- **Logging**: Records every run with timestamps in `logs/pipeline.log`
- **Automation**: Runs daily at 8 AM without manual intervention
- **Secure**: API key is stored in '.env' (not exposed in code)

## How to Run

1. Clone the repository
2. Create a `.env` file in the root folder with the following: API_KEY=your_openweathermap_api_key_here
CITY=Gaborone
3. Install dependencies: ```bash
pip install requests python-dotenv
4. Run: `python extract_weather.py`

## Project Structure

weather_pipeline/
├── extract_weather.py # Main ETL script
├── weather.db # SQLite database (created on first run)
├── logs/ # Log files
│ └── pipeline.log
|── .env #(Local only) Stores API key and city
|── .gitingnore # Prevents .env from being uploaded to Github
└── README.md 


## Technologies Used

- Python 3
- Requests (API calls)
- SQLite3 (Database)
- Task Scheduler (Automation)
- python-dotenv (Environment variable management)