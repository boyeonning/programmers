# https://school.programmers.co.kr/learn/courses/30/lessons/120861

def solution1(keyinput, board):
    result = [0,0]
    for key in keyinput:
        if key == 'right':
            if result[0]+1 > board[0] // 2:
                continue
            result[0] += 1
        if key == 'left':
            if result[0]-1 < (board[0]//2) *-1:
                continue
            result[0] -= 1
        if key == 'up':
            if result[1]+1 > board[1]//2:
                continue
            result[1] += 1
        if key == 'down':
            if result[1]-1 < (board[1]//2)*-1:
                continue
            result[1] -= 1
    return result

            
keyinput = ["down", "down", "down", "down", "down"]
board = [7, 9]
# print(solution1(keyinput, board))


def solution2(keyinput, board):
    x_lim, y_lim = board[0]//2, board[1]//2
    move = {'left' : (-1,0), 'right' : (1,0), 'up' : (0,1), 'down' : (0,-1)}
    x, y = (0,0)

    for key in keyinput:
        dx, dy = move[key]
        if abs(x+dx) > x_lim or abs(y+dy) > y_lim:
            continue
        x, y = x+dx, y+dy
    return [x,y]


print(solution2(keyinput, board))
