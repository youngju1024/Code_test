#https://school.programmers.co.kr/learn/courses/30/lessons/42627

from heapq import heappush, heappop 

def solution(jobs):
    answer = 0
    timetable = []
    jobtable = []
    n = len(jobs)
    time = 0
    for i in jobs:
        heappush(timetable,(i[0],i[1]))
    for i in range(n):
        work = heappop(timetable)
        if(len(jobtable) == 0 and time <= work[0]):
            time = work[0] + work[1]
            answer += work[1]
        else:
            while(time <= work[0]):
                if(len(jobtable) == 0):
                    break
                dowork = heappop(jobtable)
                time += dowork[0]
                answer += time-dowork[1]
            if(time <= work[0]):
                time = work[0] + work[1]
                answer += work[1]
            else:
                heappush(jobtable,(work[1],work[0]))

    
    while(len(jobtable) != 0):
        dowork = heappop(jobtable)
        time += dowork[0]
        answer += time-dowork[1]

    return answer//n
