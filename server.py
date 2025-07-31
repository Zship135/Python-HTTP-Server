
import socket
import os



class TCPServer:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def GET(self) -> bytes:
        body = "<h1>Hello World!<h1>"

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            f"Content-Length: {len(body.encode('utf-8'))}\r\n"
            "Connection: close\r\n"
            "\r\n"
            f"{body}"
        )
        return response.encode('utf-8')

    def handle_request(self, method: str) -> str:
        if method == 'GET':
            return self.GET()
        else:
            return "NONE"    

    def parse_request_line(self, data: bytes) -> bytes:
        packet = data.decode('UTF-8', errors='replace').splitlines()
        if packet:
            request_line = packet[0]
            request = request_line.split()
            method = request[0]
            path = request[1]
            version = request[2]
            print(f'Method: {method}')
            return self.handle_request(method=method)

    def start(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.host, self.port))
            sock.listen(1)
            print(f'Listening on {self.host}:{self.port}...')

            while True:
                conn, addr = sock.accept()

                with conn:
                    print(f'Connected by {addr}')
                    data = conn.recv(1024)
                    print(f'Recieved: {data.decode('UTF-8', errors='replace')}')

                    response = self.parse_request_line(data=data)
                    conn.sendall(response)
