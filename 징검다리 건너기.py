#https://school.programmers.co.kr/learn/courses/30/lessons/64062
from collections import deque

def solution(stones, k):
    answer = max(stones)
    deq = deque()
    for i in range(len(stones)):
        if deq:
            if(i-deq[0] == k):
                deq.popleft()
        while deq:
            if(stones[deq[-1]] < stones[i]):
                deq.pop()
            else:
                break
        deq.append(i)
        if(i >= k-1):
            if(stones[deq[0]] < answer):
                answer = stones[deq[0]]
    return answer