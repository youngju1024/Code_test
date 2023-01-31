#https://school.programmers.co.kr/learn/courses/30/lessons/12977

def solution(nums):
    answer = 0
    odds = []
    even = []
    even2 = []
    data = [0 for _ in range(3001)]
    for i in nums:
        if(i%2 == 1):
            odds.append(i)
        else:
            even.append(i)
    for i in range(len(odds)):
        for j in range(i+1,len(odds)):
            for k in range(j+1,len(odds)):
                data[i+j+k] += 1
    for i in range(len(even)):
        for j in range(i+1,len(even)):
            even2.append(even[i]+even[j])
    for i in odds:
        for j in even2:
            data[i+j] += 1
    prime = []
    p_data = [1 for _ in range(3001)]
    p_data[0] = 0
    p_data[1] = 0
    n = int(3001**(1/2)+1)
    for i in range(2,n):
        if(p_data[i] == 1):
            prime.append(i)
            tem = i
            while(tem <= 3000):
                p_data[tem] = 0
                tem += i
    for i in range(n,3001):
        if(p_data[i] == 1):
            prime.append(i)
    for i in prime:
        answer += data[i]
        
    return answer
