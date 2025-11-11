from flask import Flask, render_template, jsonify
import mysql.connector
from dotenv import load_dotenv
import os

# Lataa ympäristömuuttujat .env-tiedostosta
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
	# Connect to MySQL/MariaDB
	conn = mysql.connector.connect(
		host=os.getenv("DB_HOST"),
		user=os.getenv("DB_USER"),
		password=os.getenv("DB_PASSWORD"),
		database=os.getenv("DB_NAME")
	)
	cursor = conn.cursor()
	cursor.execute("SELECT NOW();")
	current_time = cursor.fetchone()[0]

	# Clean up
	cursor.close()
	conn.close()

	return render_template('index.html', current_time=current_time)

@app.route('/time')
def time():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()
    cursor.execute("SELECT NOW();")
    current_time = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return jsonify({"time": str(current_time)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
