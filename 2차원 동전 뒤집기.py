#https://school.programmers.co.kr/learn/courses/30/lessons/131703
def cal(row,tem,target):
    ret = 0
    for i in row:
        ret += i
    for i in range(len(row)):
        if (row[i] == 1):
            for j in range(len(tem)):
                tem[j][i] = (tem[j][i]+1)%2 
    for i in range(len(tem)):
        if(list(map(lambda x:(x+1)%2,tem[i])) == target[i]):
            ret += 1
        elif(tem[i] != target[i]):
            return 201
    return ret

def next_list(n,l):
    if(l[n] != 1):
        l[n] += 1
    else:
        l[n] = 0
        next_list(n+1,l)

def solution(beginning, target):
    col = len(beginning)
    row = len(beginning[0])
    minval = 201
    row_list = [0 for _ in range(row)]
    row_list[0] = -1

    for _ in range(2**row):
        next_list(0,row_list)
        tem = [[beginning[i][j] for j in range(row)] for i in range(col)]
        minval = min(minval,cal(row_list,tem,target))
    if(minval == 201):
        minval = -1
    return minval

print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]],[[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))