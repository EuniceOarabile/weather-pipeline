import sqlite3

#Connect to the database (this creates the file if it doesn't exist)
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

#Create the table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS
daily_weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        temperature REAL NOT NULL,
        humidity INTEGER NOT NULL,
        weather TEXT NOT NULL
               )

""")

conn.commit()
conn.close()

print("Database created successfully")
print("Table 'daily_weather' created successfully")