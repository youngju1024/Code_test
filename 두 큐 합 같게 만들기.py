
def solution(queue1, queue2):
    answer = 0
    sum_q1 = sum(queue1) 
    sum_q2 = sum(queue2)
    if((sum_q1 + sum_q2) % 2 == 1):
        return -1
    half = (sum_q1 + sum_q2)//2
    k = 0
    n = len(queue1) + len(queue2)
    while(k < n):
        if(sum_q1 == sum_q2):
            break
        elif(sum_q1 > sum_q2):
            tem = queue1[0]
            queue1 = queue1[1:] 
            queue2.append(tem)
            sum_q1 -= tem
            sum_q2 += tem
            answer += 1
        else:
            tem = queue2[0]
            queue2 = queue2[1:] 
            queue1.append(tem)
            sum_q2 -= tem
            sum_q1 += tem
            answer += 1
        k += 1
    if(sum_q1 != sum_q2):
        return -1
    return answer