import mysql.connector
from FlaskWebProject1 import app
from flask import jsonify
from datetime import datetime
import os

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/version")
def version():
    return jsonify({
        "instance": os.environ.get("INSTANCE_NAME"),
        "version": os.environ.get("APP_VERSION")
    })
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