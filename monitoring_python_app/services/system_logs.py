from utils.log_reader import read_log

# Default log paths for different services
LOG_PATHS = {
    "apache": {
        "error": "/var/log/apache2/error.log",
        "access": "/var/log/apache2/access.log"
    },
    "nginx": {
        "error": "/var/log/nginx/error.log",
        "access": "/var/log/nginx/access.log"
    },
    "mysql": {
        "error": "/var/log/mysql/error.log"  # Adjust if using /var/log/mysqld.log
    },
    "mongodb": {
        "log": "/var/log/mongodb/mongod.log"
    }
}

def get_logs(service, log_type="error", lines=50):
    """Fetch logs for a given service and type"""
    if service not in LOG_PATHS:
        return f"❌ Service '{service}' not found"

    service_logs = LOG_PATHS[service]

    # If log_type not found, default to first available
    file_path = service_logs.get(log_type) or list(service_logs.values())[0]

    return read_log(file_path, lines)
