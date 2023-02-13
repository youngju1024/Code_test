#https://school.programmers.co.kr/learn/courses/30/lessons/150368

def solution(users, emoticons):
    answer = []
    u = []
    for user in users:
        u.append([(-user[0]//10)*(-1),user[1]])

    combinations = []
    stack = [[]]
    while len(stack) > 0:
        simulator = stack.pop()
        if len(simulator) >= len(emoticons):
            combinations.append(simulator)
            continue
        for d in range(1, 5, 1):
            stack.append(simulator + [d])

    max_emo = 0
    max_money = 0
    combinations = [[4,4,2,4]]
    for i in combinations:
        emo = 0
        money = 0
        for user in u:    
            user_buy = 0
            for j in range(len(i)):
                if(user[0] <= i[j]):
                    user_buy += (emoticons[j]*(10-i[j]))//10
                    print(user_buy,user[1],j)
                    if(user_buy>=user[1]):
                        emo += 1
                        break
            if(user_buy<user[1]):
                money += user_buy
        if(emo > max_emo):
            max_emo = emo
            max_money = money
        elif(emo == max_emo and money > max_money):
            max_money = money

    return [max_emo,max_money]

print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],[1300, 1500, 1600, 4900]))