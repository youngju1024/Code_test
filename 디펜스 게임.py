#https://school.programmers.co.kr/learn/courses/30/lessons/142085

def solution(n, k, enemy):
    answer = 0
    max_heap = []
    for i in range(len(enemy)):
        if(n>=enemy[i]):
            n -= enemy[i]
            heappush(max_heap,(-enemy[i],enemy[i]))
            answer += 1
        elif(k > 0):
            n -= enemy[i]
            heappush(max_heap,(-enemy[i],enemy[i]))
            n += heappop(max_heap)[1]
            k -= 1
            answer += 1
        else:
            break;
    return answer

