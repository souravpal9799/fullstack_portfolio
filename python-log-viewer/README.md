# Python Log Viewer

A web-based log viewer application built with Flask that allows you to monitor and filter logs from various services in real-time.

## Features

### 🔍 **Service Selection**
- **Apache** - View Apache web server logs
- **Nginx** - View Nginx web server logs  
- **MySQL** - View MySQL database logs
- **MongoDB** - View MongoDB database logs
- **Custom Directory** - Specify custom log file paths

### 📊 **Log Type Filtering**
- **Access Logs** - View normal access and information logs
- **Error Logs** - View error, failure, and exception logs
- **All Logs** - View all logs without filtering

### 🖥️ **Real-Time Console**
- **Live Log Stream** - Continuously monitor logs in real-time
- **Auto-scroll** - Console automatically scrolls to show latest logs
- **Log Counter** - Track the number of logs received
- **Status Indicator** - Shows online/offline streaming status
- **Color-coded Logs** - Different colors for error, warning, and info logs

### 🎨 **Modern UI**
- **Responsive Design** - Works on desktop and mobile devices
- **Dark Console Theme** - Easy on the eyes for long monitoring sessions
- **Interactive Controls** - Start, stop, and clear log streams
- **Real-time Updates** - No page refresh needed

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd python-log-viewer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## Usage

### Starting a Log Stream
1. Select a service from the dropdown (Apache, Nginx, MySQL, MongoDB, or Custom)
2. Choose the log type (Access, Error, or All)
3. If using Custom service, enter the log file path
4. Click "Start Live Log Stream"

### Managing the Stream
- **Start Live Log Stream** - Begin monitoring logs
- **Stop Stream** - Stop the current log stream
- **Clear Console** - Clear all displayed logs
- **Stream Status** - Shows "Online" when actively streaming, "Offline" when stopped

### Log Filtering
- **Access Logs**: Shows normal operational logs (INFO, WARN level)
- **Error Logs**: Shows error-related logs (ERROR, FAIL, EXCEPTION keywords)
- **All Logs**: Shows all logs without filtering

## Configuration

Edit `config.py` to customize:
- Default log file paths for each service
- Log file extensions allowed
- Maximum file size limits

## API Endpoints

- `GET /api/health` - Health check endpoint
- `GET /api/{service}` - Get logs for a specific service
- `GET /api/{service}?log_type={type}` - Get filtered logs by type
- `GET /api/custom?custom_path={path}` - Get logs from custom directory

### Query Parameters
- `log_type`: `access`, `error`, or `all` (default: `all`)
- `custom_path`: Custom log file path (required for custom service)

## Sample Log File

The application includes a sample log file (`logs_debug/sample.log`) with various log types for testing:
- INFO logs (access type)
- WARNING logs (access type)  
- ERROR logs (error type)

## Features in Detail

### Real-Time Monitoring
- Logs are fetched every 2 seconds when streaming is active
- New logs appear automatically in the console
- Timestamp is added to each log entry
- Console auto-scrolls to show latest entries

### Smart Log Filtering
- **Error Detection**: Automatically identifies logs containing error-related keywords
- **Access Logs**: Excludes error-related entries for clean access monitoring
- **Flexible Filtering**: Easy to switch between log types without restarting

### Responsive Design
- Works on all screen sizes
- Mobile-friendly interface
- Optimized for both desktop and mobile monitoring

## Requirements

- Python 3.7+
- Flask
- See `requirements.txt` for complete dependencies

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).
