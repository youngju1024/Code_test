#https://school.programmers.co.kr/learn/courses/30/lessons/42891
from heapq import heappush, heappop

def solution(food_times, k):
    answer = 0
    food_num = []
    left_food_heap = []
    time = 0
    eat_each = 0
    count = 0
    for i in range(len(food_times)):
        heappush(left_food_heap,(food_times[i],i))
        food_num.append(True)
        count += food_times[i]
    if(count <= k):
        return -1
    food_count = len(food_times)
    min_eat = heappop(left_food_heap)

    while(True):
        if(k > time + (min_eat[0]-eat_each)*food_count):
            time += (min_eat[0]-eat_each)*food_count
            eat_each = min_eat[0]
            food_num[min_eat[1]] = False
            food_count -= 1
            min_eat = heappop(left_food_heap)
            while(min_eat[0] == eat_each):
                food_num[min_eat[1]] = False
                food_count -= 1
                min_eat = heappop(left_food_heap)
        else:
            n = 0
            c = (k-time)%food_count
            while(c >= 0):
                if(food_num[n]):
                    c -= 1
                n += 1
            answer = n
            break;

    return answer
