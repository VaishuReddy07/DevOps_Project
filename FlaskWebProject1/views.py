"""
Routes and views for the flask application.
"""

from datetime import datetime
from os import environ
from flask import render_template, jsonify
import mysql.connector
from FlaskWebProject1 import app

def get_db_connection():
    """Create a new MySQL connection using environment variables."""
    return mysql.connector.connect(
        host=environ.get('MYSQL_HOST', 'mysql'),
        port=int(environ.get('MYSQL_PORT', '3306')),
        user=environ.get('MYSQL_USER', 'root'),
        password=environ.get('MYSQL_PASSWORD', 'root123'),
        database=environ.get('MYSQL_DATABASE', 'mydb'),
        autocommit=True,
    )

@app.route('/version')
def version():
    """Returns application version."""
    return jsonify({"version": "2.0"})

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/mysql-time')
def mysql_time():
    """Returns the current time from the MySQL server."""
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute('SELECT CURRENT_TIMESTAMP();')
        fetched = cursor.fetchone()

        cursor.close()
        connection.close()

        if not fetched:
            return jsonify({'error': 'No timestamp returned from MySQL.'}), 500

        current_timestamp = fetched[0]

        return jsonify({
            'mysql_time': current_timestamp.isoformat()
        })

    except mysql.connector.Error as err:
        return jsonify({
            'error': str(err)
        }), 500
