import socket
from config import TWITCH_HOST, TWITCH_PORT, TWITCH_PW, TWITCH_USERNAME, TWITCH_CHANNEL

def openSocket():
    s = socket.socket()
    s.connect((TWITCH_HOST, TWITCH_PORT))
    s.send("PASS {}\r\n".format(TWITCH_PW).encode("utf-8"))
    s.send("NICK {}\r\n".format(TWITCH_USERNAME).encode("utf-8"))
    s.send("JOIN #{}\r\n".format(TWITCH_CHANNEL).encode("utf-8"))
    return s

def joinRoom(s):
    Loading = True
    while Loading:
        readbuffer_join = s.recv(1024)
        readbuffer_join = readbuffer_join.decode()
        for line in readbuffer_join.split("\n")[0:-1]:
            print(line)
            Loading = loadingComplete(line)

def loadingComplete(line):
    if ("End of /NAMES list" in line):
        print("Bot has joined " + TWITCH_CHANNEL)
        return False
    else:
        return True

def sendMessage(s, message):
    messageTemp = "PRIVMSG #" + TWITCH_CHANNEL + " :" + message
    s.send((messageTemp + "\n").encode())