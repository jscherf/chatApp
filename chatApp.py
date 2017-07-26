# Simple Chat Application

import networkMod
import sys

def heard(phrase):
    rhn = networkMod.getRemoteHostName()
    print (rhn + ": " + phrase)

if (len(sys.argv) >= 2):
    networkMod.call (sys.argv[1], whenHearCall=heard)
else:
    networkMod.wait(whenHearCall=heard)

lhn = networkMod.getLocalHostName()
print ("Start chat...")
print ("local host: " + lhn)

while networkMod.isConnected():
    phrase = input()
    
    if phrase == "quit":
        networkMod.hangUp()
    else:
        networkMod.say(phrase)
