import os

class Config:
    LOG_DIRECTORY = os.path.join(os.path.dirname(__file__), 'logs')
    DEBUG_LOG_FILE = os.path.join(os.path.dirname(__file__), 'logs_debug', 'app_debug.log')
    ALLOWED_LOG_EXTENSIONS = {'log', 'txt'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit for uploaded logs
    
    # Default log file paths for each service
    DEFAULT_LOG_PATHS = {
        'apache': '/var/log/apache2/access.log',  # Common Apache log path on Linux
        'nginx': '/var/log/nginx/access.log',      # Common Nginx log path on Linux
        'mysql': '/var/log/mysql/error.log',       # Common MySQL log path on Linux
        'mongodb': '/var/log/mongodb/mongod.log'   # Common MongoDB log path on Linux
    }
    
    SERVICE_LOGS = {
        'apache': 'services.apache.get_apache_logs',
        'nginx': 'services.nginx.get_nginx_logs',
        'mysql': 'services.mysql.get_mysql_logs',
        'mongodb': 'services.mongodb.get_mongodb_logs',
        'custom': 'services.custom.get_custom_logs'
    }