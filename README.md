Bombermanpy
===========

cf https://github.com/aybabtme/bomberman

Python library for writing clients for a bomberman game.
Receives data from the bomberman server in a separate thread.
Documented with docstrings.

Quick example
-------------

```
player = bomberman.Player(ip, port)
while True:
    print player.coords()
    player.up()
```

This creates a new player object which will connect to the specified ip and port. In a thread, the player object will receive data from the specified IP and port and update the player.data object with the new state of the game. This then loops forever, printing out the (x, y) coordinates of the player on the board and then sending over TCP to the specified IP and port the command to move up.
