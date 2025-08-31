import os
import time

def get_apache_logs(log_file_path):
    """Get Apache logs from the specified log file path"""
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
        
        # Read the last 100 lines (most recent logs)
        with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as file:
            lines = file.readlines()
            # Get the last 100 lines for performance
            recent_lines = lines[-100:] if len(lines) > 100 else lines
            
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

def get_apache_logs_tail(log_file_path, num_lines=50):
    """Get the last N lines from Apache log file (more efficient for large files)"""
    logs = []
    
    try:
        if not os.path.exists(log_file_path):
            return [f"Log file not found: {log_file_path}"]
        
        with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as file:
            # Read all lines and get the last N
            lines = file.readlines()
            if len(lines) <= num_lines:
                logs = [line.strip() for line in lines if line.strip()]
            else:
                logs = [line.strip() for line in lines[-num_lines:] if line.strip()]
        
        if logs:
            logs.insert(0, f"=== Last {len(logs)} lines from: {log_file_path} ===")
            
    except Exception as e:
        logs.append(f"Error reading log file: {str(e)}")
    
    return logs