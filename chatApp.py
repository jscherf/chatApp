# Simple Chat Application

import network
import socket
import sys

def heard(phrase):
    print("them:" + phrase)

if (len(sys.argv) >= 2):
    network.call (sys.argv[1], whenHearCall=heard)
else:
    network.wait(whenHearCall=heard)

print ("Start chat...")

while network.isConnected():
    phrase = input()
    if (phrase == "quit"):
        connection.close()
    else:
        network.say(phrase)
