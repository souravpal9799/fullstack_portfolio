def get_mongodb_logs(log_file_path):
    logs = []
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                logs.append(line.strip())
    except Exception as e:
        # Log the error to the debug log file
        with open('../logs_debug/app_debug.log', 'a') as debug_file:
            debug_file.write(f"Error reading MongoDB logs: {str(e)}\n")
    return logs