import json, socket, threading, sys

class Player:

    def __recv_update(self):
        bufsize = 1024
        bufstr = ""
        nextbufstr = ""
        while 1:
            try:
                tmpstr = self.sock.recv(bufsize)
            except:
                self.sock = None
                break
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

    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, int(port)))
        self.data = None
        thread = threading.Thread()
        thread.run = self.__recv_update
        thread.start()

    def up(self):
        try:
            self.sock.send("up\n")
        except:
            self.sock = None
            self.disconnect()

    def left(self):
        try:
            self.sock.send("left\n")
        except:
            self.sock = None
            self.disconnect()

    def down(self):
        try:
            self.sock.send("down\n")
        except:
            self.sock = None
            self.disconnect()

    def right(self):
        try:
            self.sock.send("right\n")
        except:
            self.sock = None
            self.disconnect()

    def bomb(self):
        try:
            self.sock.send("bomb\n")
        except:
            self.sock = None
            self.disconnect()

    def coords(self):
        if self.data:
            return (self.data['X'], self.data['Y'])
        return None

    def board(self):
        if self.data:
            return self.data['Board']
        return None

    def disconnect(self):
        sys.exit(0)
