import os

class Config:
    LOG_DIRECTORY = os.path.join(os.path.dirname(__file__), 'logs')
    DEBUG_LOG_FILE = os.path.join(os.path.dirname(__file__), 'logs_debug', 'app_debug.log')
    ALLOWED_LOG_EXTENSIONS = {'log', 'txt'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit for uploaded logs
    
    # Linux /var/log paths (for WSL, Docker, or Linux environments)
    DEFAULT_LOG_PATHS = {
        'apache': '/var/log/apache2/access.log',
        'nginx': '/var/log/nginx/access.log',
        'mysql': '/var/log/mysql/error.log',
        'mongodb': '/var/log/mongodb/mongod.log'
    }

    # Error log file paths for each service
    ERROR_LOG_PATHS = {
        'apache_error': '/var/log/apache2/error.log',
        'nginx_error': '/var/log/nginx/error.log',
        'mysql_error': '/var/log/mysql/error.log',
        'mongodb_error': '/var/log/mongodb/error.log'
    }
    
    # Alternative: Use Windows Event Logs (more reliable on Windows)
    USE_WINDOWS_EVENT_LOGS = False
    
    SERVICE_LOGS = {
        'apache': 'services.apache.get_apache_logs',
        'nginx': 'services.nginx.get_nginx_logs',
        'mysql': 'services.mysql.get_mysql_logs',
        'mongodb': 'services.mongodb.get_mongodb_logs',
        'custom': 'services.custom.get_custom_logs'
    }
