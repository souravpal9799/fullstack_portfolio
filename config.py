import os

class Config:
    LOG_DIRECTORY = os.path.join(os.path.dirname(__file__), 'logs')
    DEBUG_LOG_FILE = os.path.join(os.path.dirname(__file__), 'logs_debug', 'app_debug.log')
    ALLOWED_LOG_EXTENSIONS = {'log', 'txt'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit for uploaded logs
    
    # Smart Log Monitoring Configuration
    SMART_MONITORING = {
        'enabled': True,                    # Enable/disable smart monitoring
        'max_no_change_count': 5,           # Stop after N consecutive calls with no changes
        'check_interval': 2000,             # Check interval in milliseconds (2 seconds)
        'auto_restart': False,              # Auto-restart monitoring after some time
        'restart_delay': 30000,             # Delay before auto-restart (30 seconds)
        'log_change_threshold': 0.1,        # Minimum change threshold (10% of logs must change)
        'show_previous_lines': True,        # Show previous lines when no new logs detected
        'previous_lines_count': 50          # Number of previous lines to show
    }
    
    # Using log files that have actual content
    DEFAULT_LOG_PATHS = {
        'apache': '/var/log/apache2/error.log',      # Has content (693 bytes)
        'nginx': '/var/log/nginx/error.log',         # Check if exists
        'mysql': '/var/log/mysql/error.log',         # Check if exists
        'mongodb': '/var/log/mongodb/mongod.log'     # Check if exists
    }

    # Error log file paths for each service
    ERROR_LOG_PATHS = {
        'apache_error': '/var/log/apache2/error.log',
        'nginx_error': '/var/log/nginx/error.log',
        'mysql_error': '/var/log/mysql/error.log',
        'mongodb_error': '/var/log/mongodb/mongod.log'
    }
    
    # Access log file paths for each service
    ACCESS_LOG_PATHS = {
        'apache_access': '/var/log/apache2/access.log',    # Now has content (81 bytes)
        'nginx_access': '/var/log/nginx/access.log',
        'mysql_access': '/var/log/mysql/error.log',        # MySQL typically only has error logs
        'mongodb_access': '/var/log/mongodb/mongod.log'
    }
    
    # Additional system log files that have content
    SYSTEM_LOG_PATHS = {
        'syslog': '/var/log/syslog',           # Has content (351KB)
        'auth': '/var/log/auth.log',           # Has content (20KB)
        'kern': '/var/log/kern.log',           # Has content (49KB)
        'apache_combined': '/var/log/apache2/access.log'  # Apache access logs
    }
    
    # Alternative: Use Windows Event Logs (more reliable on Windows)
    USE_WINDOWS_EVENT_LOGS = False
    
    SERVICE_LOGS = {
        'apache': 'services.log_service.get_apache_logs',
        'nginx': 'services.log_service.get_nginx_logs',
        'mysql': 'services.log_service.get_mysql_logs',
        'mongodb': 'services.log_service.get_mongodb_logs',
        'custom': 'services.log_service.get_custom_logs'
    }