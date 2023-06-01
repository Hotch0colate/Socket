import time
import os
import itertools
import socket
from threading import *
from network import *
from setting import *

number = -1


def city():
    global number
    network = Network()
    number = int(network.citynumber)
    allCity = []
    while True:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        print("Your Computer Name is:" + hostname)
        print("Your Computer IP Address is:" + IPAddr)
        allCity, distance = getAllData(network)
        print("All City:", allCity)
        print("Distance: ")
        print(distance)
        time.sleep(1.5)
        os.system('cls')
        if len(allCity) == 4:
            break

    allWays = []
    way = [i for i in range(1, len(allCity)+1) if i != number]
    for i in itertools.permutations(way):
        allWays.append([number]+list(i)+[number])
    print("All Ways: ")
    print(allWays)
    time.sleep(1.5)
    minDistance = 1000
    for way in allWays:
        distanceForWay = 0
        for i in range(len(way)-1):
            distanceForWay += distance[str((way[i], way[i+1]))]

        if distanceForWay < minDistance:
            minDistance = distanceForWay
            bestWay = way

    print(f"Best Way start with {number}: ")
    print(bestWay)
    print(f"Distance: {minDistance}")
    submitDistance(network, minDistance, bestWay)


def main():
    """
    show login window and run game when login successfully
    """
    city()
    print("Thanks")


def getAllData(network):
    data = network.send({"number": number})
    return data["AllCity"], data["Distance"]


def submitDistance(network, distance, bestway):
    data = network.send({"bestway": bestway, "distance": distance})
    print("All Shortest Way: ", data["AllWay"])


main()
