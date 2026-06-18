import mysql.connector
from FlaskWebProject1 import app
from flask import jsonify
from datetime import datetime

@app.route("/")
def home():
    ...
    
@app.route("/version")
def version():
    return jsonify({"version": "1.0"})

@app.route("/db")
def db_test():
    try:
        conn = mysql.connector.connect(
            host="mysql",
            user="root",
            password="root123",
            database="mysql"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return f"""
        <h2>MySQL Connected Successfully!</h2>
        <p>Database Time: {result[0]}</p>
        """

    except Exception as e:
        return f"""
        <h2>Database Connection Failed</h2>
        <p>{str(e)}</p>
        """, 500