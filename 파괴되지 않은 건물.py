# https://school.programmers.co.kr/learn/courses/30/lessons/92344

def heal(a,b,c,d,heal,board):
    min_x = min(a,c)
    min_y = min(b,d)
    max_x = max(a,c)+1
    max_y = max(b,d)+1

    board[min_x][min_y] += heal
    board[max_x][min_y] -= heal
    board[min_x][max_y] -= heal
    board[max_x][max_y] += heal

def damage(a,b,c,d,dam,board):
    min_x = min(a,c)
    min_y = min(b,d)
    max_x = max(a,c)+1
    max_y = max(b,d)+1

    board[min_x][min_y] -= dam
    board[max_x][min_y] += dam
    board[min_x][max_y] += dam
    board[max_x][max_y] -= dam

def check(board):
    ret = 0
    for i in board:
        for data in i:
            if(data > 0):
                ret += 1
    return ret

def add(board,b,row,col):
    for i in range(col+1):
        for j in range(1,row+1):
            b[i][j] += b[i][j-1]
    for j in range(row+1):
        for i in range(1,col+1):
            b[i][j] += b[i-1][j]
    for i in range(col):
        for j in range(row):
            board[i][j] += b[i][j]

def solution(board, skill):
    answer = 0
    row = len(board[0])
    col = len(board)
    b = [[0 for i in range(row+1)] for j in range(col+1)]
    for i in skill:
        if(i[0] == 1):
            damage(i[1],i[2],i[3],i[4],i[5],b)
        else:
            heal(i[1],i[2],i[3],i[4],i[5],b)
    add(board,b,row,col)
    answer = check(board)
    return answer
