import json, socket, threading, sys

class Player:
    """A class representing a bomberman player."""

    def __recv_update(self):
        """Loop forever reading updates from self.sock"""
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
        """Initialize the player by connecting to and receiving data from the server"""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, int(port)))
        self.data = None
        thread = threading.Thread()
        thread.run = self.__recv_update
        thread.start()

    def up(self):
        """Move the Player up"""
        try:
            self.sock.send("up\n")
        except:
            self.sock = None
            self.disconnect()

    def left(self):
        """Move the Player left"""
        try:
            self.sock.send("left\n")
        except:
            self.sock = None
            self.disconnect()

    def down(self):
        """Move the Player down"""
        try:
            self.sock.send("down\n")
        except:
            self.sock = None
            self.disconnect()

    def right(self):
        """Move the Player right"""
        try:
            self.sock.send("right\n")
        except:
            self.sock = None
            self.disconnect()

    def bomb(self):
        """Make the Player place a bomb"""
        try:
            self.sock.send("bomb\n")
        except:
            self.sock = None
            self.disconnect()

    def coords(self):
        """Returns None or the (x,y) coordinates of the Player"""
        if self.data:
            return (self.data['X'], self.data['Y'])
        return None

    def board(self):
        """Returns None or a two dimensional array of dicts that is the board"""
        if self.data:
            return self.data['Board']
        return None

    def disconnect(self):
        """Default function to run upon a disconnect"""
        sys.exit(0)
