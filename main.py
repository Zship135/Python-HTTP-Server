from server import TCPServer
import os
from dotenv import load_dotenv



load_dotenv()

HOST = str(os.getenv('HOST_IP'))
PORT = int(os.getenv('PORT'))

def main() -> None:
    server = TCPServer(HOST, PORT)
    server.start()

if __name__ == '__main__':
    main()
