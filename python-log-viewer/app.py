from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from api.routes import api_bp

app = Flask(__name__)

# Load configuration from config.py
app.config.from_pyfile('config.py')

# Set up logging
handler = RotatingFileHandler('logs_debug/app_debug.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# Register API routes
app.register_blueprint(api_bp)

@app.route('/')
def index():
    return "Welcome to the Flask Log Viewer!"

if __name__ == '__main__':
    app.run(debug=True)