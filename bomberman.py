import json, socket, threading

class Player:

    def __recv_update(self):
        bufsize = 1024
        bufstr = ""
        nextbufstr = ""
        while 1:
            tmpstr = self.sock.recv(bufsize)
            bufstr += tmpstr
            if '\n' not in tmpstr:
                continue
            bufarr = bufstr.split('\n')
            bufstr = bufarr[0]
            nextbufstr = bufarr[1]
            try:
                self.data = json.loads(bufstr)
                print self.data
            except ValueError:
                bufstr = ""
                nextbufstr = ""
                continue
            bufstr = nextbufstr
            nextbufstr = ""

    def __init__(self, ip, port):
        bufsize = 1024
        bufstr = ""
        nextbufstr = ""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, int(port)))
        self.data = None
        thread = threading.Thread()
        thread.run = self.__recv_update
        thread.start()
        
    def up(self):
        self.sock.send("up\n")

    def left(self):
        self.sock.send("left\n")

    def down(self):
        self.sock.send("down\n")

    def right(self):
        self.sock.send("right\n")

    def bomb(self):
        self.sock.send("bomb\n")

    def coords(self):
        if self.data:
            return (self.data['X'], self.data['Y'])
        return None

    def board(self):
        if self.data:
            return self.data['Board']
        return None
