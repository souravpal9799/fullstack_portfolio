# Flask Log Viewer

## Overview
Flask Log Viewer is a web application built with Flask that allows users to view logs from various services such as Apache, Nginx, MySQL, MongoDB, and custom log directories. The application provides a structured API for selecting services and displaying logs in the browser.

## Features
- View logs from Apache, Nginx, MySQL, MongoDB, and custom directories.
- Structured API for easy access to logs.
- Detailed logging for debugging purposes.

## Project Structure
```
flask-log-viewer
├── app.py                # Entry point of the Flask application
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
├── config.py             # Configuration settings
├── logs                  # Directory for custom logs (initially empty)
├── services              # Service-specific log handling modules
│   ├── __init__.py
│   ├── apache.py
│   ├── nginx.py
│   ├── mysql.py
│   ├── mongodb.py
│   └── custom.py
├── api                   # API-related modules
│   ├── __init__.py
│   ├── routes.py
│   └── utils.py
├── templates             # Frontend templates
│   └── index.html
├── static                # Static files (CSS)
│   └── style.css
└── logs_debug            # Debug log files
    └── app_debug.log
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-log-viewer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000` to view the logs.

## Logging
The application logs detailed information to `logs_debug/app_debug.log` to assist in troubleshooting and debugging. Ensure that the log directory is writable by the application.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.