#!/usr/bin/python2
import json, socket, threading.Thread

class Player:

    def __recv_update():
        bufstr = ""
        nextbufstr = ""
        while 1:
            tmpstr = sock.recv(bufsize)
            bufstr += tmpstr
            if '\n' not in tmpstr:
                continue
            bufarr = bufstr.split('\n')
            bufstr = bufarr[0]
            nextbufstr = bufarr[1]
            try:
                self.data = json.loads(bufstr)
            except ValueError:
                bufstr = ""
                nextbufstr = ""
                continue
            bufstr = nextbufstr
            nextbufstr = ""

    def __init__(ip, port):
        bufsize = 1024
        bufstr = ""
        nextbufstr = ""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        directions = ["up\n", "left\n", "right\n", "down\n"]
        self.data = None
        thread = Thread()
        thread.run = self.__recv_update
        thread.start()
        
    def up():
        self.sock.send("up\n")

    def left():
        self.sock.send("left\n")

    def down():
        self.sock.send("down\n")

    def right():
        self.sock.send("right\n")

    def bomb():
        self.sock.send("bomb\n")

    def coords():
        if data:
            return (data['X'], data['Y'])
        return None

    def board():
        if data:
            return data['Board']
        return None
