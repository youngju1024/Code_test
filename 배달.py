#https://school.programmers.co.kr/learn/courses/30/lessons/12978

def min_node(ret,is_min):
    min_val = 500002
    min_node = -1
    for i in range(len(ret)):
        if(ret[i] < min_val and is_min[i] == False):
            min_val = ret[i]
            min_node = i
    return min_node

def solution(N, road, K):
    answer = 0
    mat = [[500001 for _ in range(N)] for _ in range(N)]
    is_min = [False for _ in range(N)]

    ret = [500001 for _ in range(N)]
    for i in range(N):
        mat[i][i] = 0
    for i in road:
        if(mat[i[0]-1][i[1]-1] > i[2]):
            mat[i[0]-1][i[1]-1] = i[2]
            mat[i[1]-1][i[0]-1] = i[2]
    
    for i in range(N):
        if(mat[0][i] < ret[i]):
            ret[i] = mat[0][i]
    ret[0] = 0
    is_min[0] = True

    for _ in range(N-1):
        i = min_node(ret,is_min)
        is_min[i] = True
        for j in range(N):
            if(ret[i] + mat[i][j] < ret[j] and is_min[j] == False):
                ret[j] = ret[i] + mat[i][j]

    for i in ret:
        if(i <= K):
            answer += 1
    return answer
