import os
import time

def get_logs(log_file_path, service_name="custom", max_lines=100):
    """
    Universal log reading function that works for all services.
    Returns logs from the specified log file path.
    """
    logs = []
    
    try:
        # Check if file exists
        if not os.path.exists(log_file_path):
            return [f"Log file not found: {log_file_path}"]
        
        # Check if file is readable
        if not os.access(log_file_path, os.R_OK):
            return [f"Permission denied reading log file: {log_file_path}"]
        
        # Get file size
        file_size = os.path.getsize(log_file_path)
        if file_size == 0:
            return ["Log file is empty"]
        
        # Read the last N lines (most recent logs)
        with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as file:
            lines = file.readlines()
            # Get the last N lines for performance
            recent_lines = lines[-max_lines:] if len(lines) > max_lines else lines
            
            for line in recent_lines:
                line = line.strip()
                if line:  # Skip empty lines
                    logs.append(line)
        
        # Add file info
        if logs:
            logs.insert(0, f"=== Reading from: {log_file_path} (Last {len(logs)} lines, File size: {file_size} bytes) ===")
        
    except FileNotFoundError:
        logs.append(f"Log file not found: {log_file_path}")
    except PermissionError:
        logs.append(f"Permission denied: {log_file_path}")
    except UnicodeDecodeError as e:
        logs.append(f"Encoding error reading log file: {str(e)}")
    except Exception as e:
        logs.append(f"Error reading log file: {str(e)}")
    
    return logs

def get_custom_logs(log_directory):
    """
    Get logs from a custom directory containing multiple log files.
    """
    logs = []
    try:
        if os.path.isfile(log_directory):
            # If it's a single file, read it directly
            return get_logs(log_directory, "custom")
        
        # If it's a directory, read all .log files
        for filename in os.listdir(log_directory):
            if filename.endswith('.log'):
                file_path = os.path.join(log_directory, filename)
                file_logs = get_logs(file_path, "custom")
                logs.extend(file_logs)
                
    except Exception as e:
        logs.append(f"Error reading custom logs: {str(e)}")
    
    return logs

# Service-specific wrapper functions for backward compatibility
def get_apache_logs(log_file_path):
    """Get Apache logs from the specified log file path"""
    return get_logs(log_file_path, "apache")

def get_nginx_logs(log_file_path):
    """Get Nginx logs from the specified log file path"""
    return get_logs(log_file_path, "nginx")

def get_mysql_logs(log_file_path):
    """Get MySQL logs from the specified log file path"""
    return get_logs(log_file_path, "mysql")

def get_mongodb_logs(log_file_path):
    """Get MongoDB logs from the specified log file path"""
    return get_logs(log_file_path, "mongodb")
