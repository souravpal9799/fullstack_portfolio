from flask import Flask, render_template
import logging
from logging.handlers import RotatingFileHandler
from api.routes import api

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
app.register_blueprint(api)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)