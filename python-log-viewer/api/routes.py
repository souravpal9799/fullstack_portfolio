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
    log_path = custom_path if custom_path else Config.DEFAULT_LOG_PATHS['apache']
    logs = get_apache_logs(log_path)
    return jsonify(logs)

@api.route('/api/nginx', methods=['GET'])
def nginx_logs():
    # Get custom path from query params or use default
    custom_path = request.args.get('custom_path')
    log_path = custom_path if custom_path else Config.DEFAULT_LOG_PATHS['nginx']
    logs = get_nginx_logs(log_path)
    return jsonify(logs)

@api.route('/api/mysql', methods=['GET'])
def mysql_logs():
    # Get custom path from query params or use default
    custom_path = request.args.get('custom_path')
    log_path = custom_path if custom_path else Config.DEFAULT_LOG_PATHS['mysql']
    logs = get_mysql_logs(log_path)
    return jsonify(logs)

@api.route('/api/mongodb', methods=['GET'])
def mongodb_logs():
    logs = get_mongodb_logs()
    return jsonify(logs)

@api.route('/api/custom', methods=['GET'])
def custom_logs():
    custom_path = request.args.get('custom_path')
    if not custom_path:
        return jsonify({"error": "Custom path is required"}), 400
    logs = get_custom_logs(custom_path)
    return jsonify(logs) if logs else jsonify({"error": "No logs found"}), 404