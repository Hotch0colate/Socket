import socket
import json
from setting import *


class Network:
    def __init__(self):
        """
        set default value of network for multiplayer game
        """
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.addr = (self.server, self.port)
        self.citynumber = self.connect()

    def disconnect(self):
        """
        disconnect from server
        """
        self.client.close()

    def connect(self):
        """
        get first information from server

        Returns:
            Player: player information
        """
        self.client.connect(self.addr)
        return self.client.recv(65536).decode('utf-8')

    def send(self, data):
        self.client.send(json.dumps(data).encode('utf-8'))
        print("send data: ")
        print(data)
        responce = json.loads(self.client.recv(65536))
        return responce
