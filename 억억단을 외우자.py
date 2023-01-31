#https://school.programmers.co.kr/learn/courses/30/lessons/138475

def solution(e, starts):
    data = [0 for i in range(e+1)]
    answer = []
    for i in range(1,e+1):
        for j in range(i+1,e//i+1):
            data[i*j] += 2
    for i in range(1,int((e**(1/2))+1)):
        data[i**2] += 1

    max_val = 0
    max_val_index = 0
    for i in range(e,0,-1):
        if(data[i] >= max_val):
            max_val = data[i]
            max_val_index = i
            data[i] = i
        else:
            data[i] = max_val_index

    for i in starts:
        answer.append(data[i])
    return answer
