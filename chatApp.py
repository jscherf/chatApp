# Simple Chat Application

import networkMod
import sys

def heard(phrase):
    rhn = networkMod.getRemoteHostName()
    print(rhn + ":" + phrase)

if (len(sys.argv) >= 2):
    networkMod.call (sys.argv[1], whenHearCall=heard)
else:
    networkMod.wait(whenHearCall=heard)

print ("Start chat...")

while networkMod.isConnected():
    phrase = input()
    networkMod.say(phrase)
