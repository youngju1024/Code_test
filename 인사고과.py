#https://school.programmers.co.kr/learn/courses/30/lessons/152995
from heapq import heappush, heappop

def solution(scores):
    answer = 1
    lis = []
    wanho1 = scores[0][0]
    wanho2 = scores[0][1]
    wanho_sum = wanho1 + wanho2
    for i in range(len(scores)):
        data = scores[i]
        heappush(lis,(-data[0]-data[1],i,data[0],data[1]))
    
    up = []
    while(lis):
        tem = heappop(lis)
        if(tem[1] == 0):
            break
        else:
            up.append([tem[2],tem[3]])

    up = sorted(up,key = lambda x : (-x[0],x[1]))

    max2 = 0
    for data in up:
        if(wanho1 < data[0] and wanho2 < data[1]):
            return -1
        if(max2 <= data[1]):
            answer += 1
            max2 = data[1]

    return answer