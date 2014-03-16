#!/usr/bin/python2
import bomberman, copy, random, sys, time

def disconnect():
    pass

def run_ai():
    while 1:
        try:
            player = bomberman.Player(sys.argv[1], sys.argv[2])
            break
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            continue
    player.disconnect = disconnect
    directions = [player.up, player.down, player.left, player.right]
    nextmove = random.choice(directions)
    nextmove()
    while 1:
        if player.sock == None:
            break
        def score_move(board, move, x, y, n):
            if n >= 10:
                return 0
            if move == player.up:
                y -= 1
            if move == player.down:
                y += 1
            if move == player.left:
                x -= 1
            if move == player.right:
                x += 1
            if y == 0 or x == 0:
                return 0
            if y == len(board[x-1]) - 1 or x == len(board) - 1:
                return 0
            if board[x][y]['Name'] != "Ground":
                return 0
            retval = 1
            if board[x-1][y]['Name'] == "Ground":
                retval += 1
            if board[x+1][y]['Name'] == "Ground":
                retval += 1
            if board[x][y-1]['Name'] == "Ground":
                retval += 1
            if board[x][y+1]['Name'] == "Ground":
                retval += 1
            for nextmove in directions:
                if (nextmove == player.up and move == player.down) or \
                (nextmove == player.down and move == player.up) or \
                (nextmove == player.left and move == player.right) or \
                (nextmove == player.right and move == player.left):
                    continue
            retval += score_move(board, nextmove, x, y, n+1)
            return retval

        if player.data:
            x, y = player.coords()
            board = player.board()
            scores = []
            for move in directions:
                scores.append(score_move(board, move, x, y, 0))
            directions[scores.index(max(scores))]()
        time.sleep(0.5)

while 1:
    try:
        run_ai()
    except KeyboardInterrupt:
        sys.exit(0)
