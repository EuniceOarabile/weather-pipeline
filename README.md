# Weather ETL Pipeline

A fully automated Python pipeline that extracts live weather data from the OpenWeatherMap API, transforms it, and loads it into a SQLite database. The pipeline runs daily at 8 AM via Windows Task Scheduler.

## Features

- **Extract**: Pulls current weather data for Gaborone, Botswana
- **Transform**: Parses JSON and extracts temperature, humidity, and weather description
- **Load**: Appends clean data to a SQLite database (`weather.db`)
- **Logging**: Records every run with timestamps in `logs/pipeline.log`
- **Automation**: Runs daily at 8 AM without manual intervention

## How to Run

1. Clone the repository
2. Install dependencies: `pip install requests`
3. Replace `API_KEY` in `extract_weather.py` with your OpenWeatherMap API key
4. Run: `python extract_weather.py`

## Project Structure

weather_pipeline/
├── extract_weather.py # Main ETL script
├── weather.db # SQLite database (created on first run)
├── logs/ # Log files
│ └── pipeline.log
└── README.md


## Technologies Used

- Python 3
- Requests (API calls)
- SQLite3 (Database)
- Task Scheduler (Automation)