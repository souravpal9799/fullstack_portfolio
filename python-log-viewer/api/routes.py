from flask import Blueprint, jsonify, request
from services.apache import get_apache_logs
from services.nginx import get_nginx_logs
from services.mysql import get_mysql_logs
from services.mongodb import get_mongodb_logs
from services.custom import get_custom_logs
from config import Config

api = Blueprint('api', __name__)

@api.route('/api/health')
def health():
    return {"status": "ok"}

@api.route('/api/apache', methods=['GET'])
def apache_logs():
    # Get custom path from query params or use default
    custom_path = request.args.get('custom_path')
    log_type = request.args.get('log_type', 'all')
    
    if custom_path:
        log_path = custom_path
    elif log_type == 'error':
        log_path = Config.ERROR_LOG_PATHS['apache_error']
    elif log_type == 'access':
        log_path = Config.ACCESS_LOG_PATHS['apache_access']
    else:
        log_path = Config.DEFAULT_LOG_PATHS['apache']
    
    logs = get_apache_logs(log_path)
    
    # Filter logs based on log_type if specified
    if log_type != 'all':
        logs = filter_logs_by_type(logs, log_type)
    
    return jsonify({"logs": logs})

@api.route('/api/nginx', methods=['GET'])
def nginx_logs():
    # Get custom path from query params or use default
    custom_path = request.args.get('custom_path')
    log_type = request.args.get('log_type', 'all')
    
    if custom_path:
        log_path = custom_path
    elif log_type == 'error':
        log_path = Config.ERROR_LOG_PATHS['nginx_error']
    elif log_type == 'access':
        log_path = Config.ACCESS_LOG_PATHS['nginx_access']
    else:
        log_path = Config.DEFAULT_LOG_PATHS['nginx']
    
    logs = get_nginx_logs(log_path)
    
    # Filter logs based on log_type if specified
    if log_type != 'all':
        logs = filter_logs_by_type(logs, log_type)
    
    return jsonify({"logs": logs})

@api.route('/api/mysql', methods=['GET'])
def mysql_logs():
    # Get custom path from query params or use default
    custom_path = request.args.get('custom_path')
    log_type = request.args.get('log_type', 'all')
    
    if custom_path:
        log_path = custom_path
    elif log_type == 'error':
        log_path = Config.ERROR_LOG_PATHS['mysql_error']
    elif log_type == 'access':
        log_path = Config.ACCESS_LOG_PATHS['mysql_access']
    else:
        log_path = Config.DEFAULT_LOG_PATHS['mysql']
    
    logs = get_mysql_logs(log_path)
    
    # Filter logs based on log_type if specified
    if log_type != 'all':
        logs = filter_logs_by_type(logs, log_type)
    
    return jsonify({"logs": logs})

@api.route('/api/mongodb', methods=['GET'])
def mongodb_logs():
    log_type = request.args.get('log_type', 'all')
    
    if log_type == 'error':
        log_path = Config.ERROR_LOG_PATHS['mongodb_error']
    elif log_type == 'access':
        log_path = Config.ACCESS_LOG_PATHS['mongodb_access']
    else:
        log_path = Config.DEFAULT_LOG_PATHS['mongodb']
    
    logs = get_mongodb_logs(log_path)
    
    # Filter logs based on log_type if specified
    if log_type != 'all':
        logs = filter_logs_by_type(logs, log_type)
    
    return jsonify({"logs": logs})

@api.route('/api/custom', methods=['GET'])
def custom_logs():
    custom_path = request.args.get('custom_path')
    log_type = request.args.get('log_type', 'all')
    
    if not custom_path:
        return jsonify({"error": "Custom path is required"}), 400
    
    logs = get_custom_logs(custom_path)
    
    if not logs:
        return jsonify({"error": "No logs found"}), 404
    
    # Filter logs based on log_type if specified
    if log_type != 'all':
        logs = filter_logs_by_type(logs, log_type)
    
    return jsonify({"logs": logs})

def filter_logs_by_type(logs, log_type):
    """Filter logs based on the specified log type"""
    if not logs:
        return []
    
    filtered_logs = []
    for log in logs:
        log_str = str(log).lower()
        
        if log_type == 'error':
            # Include logs that contain error-related keywords
            if any(keyword in log_str for keyword in ['error', 'fail', 'exception', 'critical', 'fatal']):
                filtered_logs.append(log)
        elif log_type == 'access':
            # Exclude logs that contain error-related keywords
            if not any(keyword in log_str for keyword in ['error', 'fail', 'exception', 'critical', 'fatal']):
                filtered_logs.append(log)
        else:
            # 'all' type - include everything
            filtered_logs.append(log)
    
    return filtered_logs