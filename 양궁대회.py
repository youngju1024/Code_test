#https://school.programmers.co.kr/learn/courses/30/lessons/92342

max_score = 0
max_score_record = [-1]

def calc_score(lion_shot,apeach_shot):
    lion = 0
    apeach = 0
    for i in range(11):
        if(lion_shot[i] > apeach_shot[i]):
            lion += 10-i
        elif(apeach_shot[i] > 0):
            apeach += 10-i
    return lion - apeach

def DFS(n,idx,info,lion_shot):
    global max_score, max_score_record
    if(idx == -1 or n == 0):
        lion_shot[10] = n
        n = 0
        
        score = calc_score(lion_shot,info)
        if(score > max_score):
            max_score = score
            max_score_record = []
            for i in lion_shot:
                max_score_record.append(i)
        lion_shot[10] = 0

    else:
        if(n > info[idx]):
            lion_shot[idx] = info[idx] + 1
            DFS(n - lion_shot[idx],idx-1,info,lion_shot)
        lion_shot[idx] = 0
        DFS(n,idx-1,info,lion_shot)

def solution(n, info):
    global max_score_record
    DFS(n,9,info,[0,0,0,0,0,0,0,0,0,0,0])
    answer = max_score_record
    

    return answer