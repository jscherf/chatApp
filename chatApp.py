# Simple Chat Application

import networkMod
import sys

def heard(phrase):
    rhn = network.getRemoteHostName()
    print(rhn + ":" + phrase)

if (len(sys.argv) >= 2):
    network.call (sys.argv[1], whenHearCall=heard)
else:
    network.wait(whenHearCall=heard)

print ("Start chat...")

while network.isConnected():
    phrase = input()
    network.say(phrase)
