# HTTP Server From Scratch in Python

A lightweight HTTP server implementation built from scratch using Python's socket library. This server handles basic HTTP GET requests and serves content from a configurable directory.

## Features

- **Pure Python Implementation**: Built using only Python's standard library
- **Environment Configuration**: Configurable host and port via environment variables
- **Path Security**: Built-in path traversal protection
- **Simple HTTP Response**: Handles basic GET requests with proper HTTP headers
- **Connection Logging**: Logs incoming connections and requests

## Requirements

- Python 3.6+
- `python-dotenv` package

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Install dependencies:
```bash
pip install python-dotenv
```

3. Create a `.env` file in the project root:
```env
HOST_IP=<host_ip>
PORT=<port>
```

## Usage

Run the server:
```bash
python main.py
```

The server will start listening on the configured host and port. You can then access it via:
```
http://<host_ip>:<port>
```

## Project Structure

```
.
├── main.py          # Entry point and server initialization
├── server.py        # TCPServer class implementation
├── .env            # Environment configuration (create this)
└── README.md       # This file
```

## Configuration

The server can be configured using environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `HOST_IP` | Server bind address | Required |
| `PORT` | Server port number | Required |

## Code Overview

### TCPServer Class

The main server class handles:
- Socket creation and binding
- HTTP request parsing
- Path resolution with security checks
- Response generation

### Key Methods

- `start()`: Initializes the server socket and handles incoming connections
- `parse_request_line()`: Parses incoming HTTP requests
- `handle_request()`: Routes requests to appropriate handlers
- `GET()`: Handles HTTP GET requests

## Security Features

- **Input Sanitization**: Request data is properly decoded with error handling

## Example Response

The server currently returns a simple HTML response:
```html
<h1>Hello World!</h1>
```

## Development

To extend the server functionality:

1. Add new HTTP methods in the `handle_request()` method
2. Implement file serving by enhancing the `GET()` method
3. Add support for different content types
4. Implement request routing

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).
