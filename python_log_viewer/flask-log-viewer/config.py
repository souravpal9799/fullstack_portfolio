import os

class Config:
    LOG_DIRECTORY = os.path.join(os.path.dirname(__file__), 'logs')
    DEBUG_LOG_FILE = os.path.join(os.path.dirname(__file__), 'logs_debug', 'app_debug.log')
    ALLOWED_LOG_EXTENSIONS = {'log', 'txt'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit for uploaded logs
    SERVICE_LOGS = {
        'apache': 'services.apache.get_apache_logs',
        'nginx': 'services.nginx.get_nginx_logs',
        'mysql': 'services.mysql.get_mysql_logs',
        'mongodb': 'services.mongodb.get_mongodb_logs',
        'custom': 'services.custom.get_custom_logs'
    }