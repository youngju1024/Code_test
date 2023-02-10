#https://school.programmers.co.kr/learn/courses/30/lessons/68646

def solution(a):
    answer = 0
    min_l = a[0]
    min_list = [a[0]]
    for i in a[1:]:
        if(min_l>i):
            min_l = i
            min_list.append(i)
    min_l = a[-1]
    min_list.append(a[-1])
    for i in list(reversed(a[:-1])):
        if(min_l>i):
            min_l = i
            min_list.append(i)
    answer = len(min_list)-1    
    
    return answer