def format_log_entry(log_entry):
    # Function to format a single log entry for display
    return log_entry.strip()

def handle_error(error_message):
    # Function to handle errors and log them
    import logging
    logging.error(error_message)
    return {"error": error_message}, 500

def validate_log_file_path(file_path):
    # Function to validate the provided log file path
    import os
    if not os.path.isfile(file_path):
        handle_error(f"Log file does not exist: {file_path}")
        return False
    return True

def get_last_n_lines(file_path, num_lines=50):
    """
    Get the last N lines from a log file efficiently.
    Returns a list of log lines with file information.
    """
    import os
    
    logs = []
    
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            return [f"Log file not found: {file_path}"]
        
        # Check if file is readable
        if not os.access(file_path, os.R_OK):
            return [f"Permission denied reading log file: {file_path}"]
        
        # Get file size
        file_size = os.path.getsize(file_path)
        if file_size == 0:
            return ["Log file is empty"]
        
        # Read the last N lines
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            lines = file.readlines()
            
            # Get the last N lines, filtering out empty lines
            if len(lines) <= num_lines:
                recent_lines = [line.strip() for line in lines if line.strip()]
            else:
                recent_lines = [line.strip() for line in lines[-num_lines:] if line.strip()]
            
            logs.extend(recent_lines)
        
        # Add file info header
        if logs:
            logs.insert(0, f"=== Previous {len(logs)} lines from: {file_path} (File size: {file_size} bytes) ===")
        
    except FileNotFoundError:
        logs.append(f"Log file not found: {file_path}")
    except PermissionError:
        logs.append(f"Permission denied: {file_path}")
    except UnicodeDecodeError as e:
        logs.append(f"Encoding error reading log file: {str(e)}")
    except Exception as e:
        logs.append(f"Error reading log file: {str(e)}")
    
    return logs