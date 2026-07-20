import requests
import sqlite3
from datetime import datetime
import logging
import os

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = os.getenv("CITY")

#Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
   filename="logs/pipeline.log",
   level=logging.INFO,
   format="%(asctime)s - %(levelname)s - %(message)s"
)

API_KEY = os.getenv("API_KEY")
CITY = "Gaborone"
URL = f"https://api.openweathermap.org/data/2.5/weather?q=Gaborone&appid=3e636aac71cfc416bf2964dbe73d85e4&units=metric"

logging.info("=== Pipeline started ===")

response = requests.get(URL)
print(response.text)
data = response.json()

logging.info("API call successful")

data=response.json()
print(data["name"])
print(data["main"]["temp"])
print(data["main"]["humidity"])
print(data["weather"][0]["description"])

logging.info(f"Extracted: {data['name']}, {data['main']['temp']}°C, {data['main']['humidity']}%")

#Get current timestamp
timestamp = datetime.now().isoformat()

#Insert into database
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute("""
    INSERT INTO daily_weather (date, temperature, humidity, weather)
    VALUES (?, ?, ?, ?)
""", (
    timestamp,
    #this is the date
    data["main"]["temp"],
    data["main"]["humidity"],
    data["weather"][0]["description"]
))

conn.commit()
conn.close()

logging.info("Data inserted into database successfully")
logging.info("Pipeline completed successfully")

print("Data inserted into database")