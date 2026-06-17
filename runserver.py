from os import environ
from FlaskWebProject1 import app

if __name__ == '__main__':
    # 1. Safely extract the port from environment variables, fallback to 8080
    try:
        PORT = int(environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 8080

    # 2. Define the HOST variable so flake8/Python doesn't crash
    HOST = '0.0.0.0'
        
    # 3. Start the Flask application exactly once with the correct parameters
    app.run(host=HOST, port=PORT)