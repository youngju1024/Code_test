#https://school.programmers.co.kr/learn/courses/30/lessons/77486

def solution(enroll, referral, seller, amount):
    answer = []
    moneylist = {}
    parent = {}
    for i in range(len(enroll)):
        if(referral[i] == "-"):
            parent[enroll[i]] = "center"
        else:
            parent[enroll[i]] = referral[i]
        moneylist[enroll[i]] = 0
    for i in range(len(seller)):
        money = amount[i]*100
        saleman = seller[i]
        while(True):
            tax = money//10
            moneylist[saleman] += money - tax 
            saleman = parent[saleman]
            if(tax == 0 or saleman == "center"):
                break
            money = tax
    for i in moneylist.values():
        answer.append(i)
    return answer
