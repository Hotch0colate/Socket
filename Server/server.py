import socket
import json
from threading import *

print("hello")
server = "192.168.1.100"  # Localhost
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
allShortestWay = []

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(5)
print("Waiting for a connection, Server Started")


def threaded_client(conn, number, distance):
    """
    start thread for each client to receive data from server

    Args:
        conn (socket): connection from client
        player (int): id of player
    """
    global allShortestWay
    conn.send(f"{number}".encode('utf-8'))
    # reply = ""
    while True:
        try:
            data = json.loads(conn.recv(65536))

            if not data:
                print("Disconnected")
                break
            else:
                reply = {"AllCity": citynumberlist,
                         "Distance": distance}

            conn.sendall(json.dumps(reply).encode('utf-8'))
        except Exception as e:
            print(e)
            break
        if len(citynumberlist) == 4:
            break

    data = json.loads(conn.recv(65536))
    bestway = data["bestway"]
    allShortestWay += [bestway]
    distance = data["distance"]
    while len(allShortestWay) != 4:
        continue

    if (number == 1):
        print("All Shortest Way:", allShortestWay)
        print("Distance: ", distance)

    reply = {"AllWay": allShortestWay,
             "Distance": distance}
    conn.sendall(json.dumps(reply).encode('utf-8'))
    conn.close()


def main():
    """
    start server wait for client to connect
    and check number of player and decide 
    which client will be which id
    """
    global citynumberlist
    global distance
    citynumberlist = []
    distance = {
        "(1, 2)": 10,
        "(1, 3)": 15,
        "(1, 4)": 20,
        "(2, 1)": 10,
        "(2, 3)": 35,
        "(2, 4)": 25,
        "(3, 1)": 15,
        "(3, 2)": 35,
        "(3, 4)": 30,
        "(4, 1)": 20,
        "(4, 2)": 25,
        "(4, 3)": 30,
    }
    number = 1
    while True:
        conn, addr = s.accept()
        citynumberlist += [number]
        thread = Thread(target=threaded_client, args=(conn, number, distance))
        thread.start()
        number += 1


main()
