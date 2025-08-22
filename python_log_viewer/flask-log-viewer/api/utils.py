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