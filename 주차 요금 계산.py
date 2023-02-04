#https://school.programmers.co.kr/learn/courses/30/lessons/92341
from heapq import heappush,heappop
import math

def cal_time(in_t,out_t):
    i = in_t.split(':')
    o = out_t.split(':')
    return (int(o[0])-int(i[0]))*60 + int(o[1])-int(i[1])

def cal_fee(time_dif,fees):
    if(fees[0] >= time_dif):
        return fees[1]
    else:
        return fees[1] + math.ceil((time_dif-fees[0])/fees[2])*fees[3]

def solution(fees, records):
    answer = []
    car = []
    in_time = []
    time = []
    for i in records:
        tem = i.split(' ')
        if(tem[1] not in car):
            car.append(tem[1])
            time.append(0)
            in_time.append('0')
        k = car.index(tem[1])
        if(tem[2] == "IN"):
            in_time[k] = tem[0]
        elif(tem[2] == "OUT"):
            time[k] += cal_time(in_time[k],tem[0])
            in_time[k] = -1
    for i in range(len(in_time)):
        if(in_time[i] != -1):
            time[i] += cal_time(in_time[i],"23:59")
    minheap = []
    for i in range(len(time)):
        heappush(minheap,(car[i],cal_fee(time[i],fees)))
    for i in range(len(time)):
        answer.append(heappop(minheap)[1])
    return answer

print(solution([1, 461, 1, 10],["00:00 1234 IN"]))