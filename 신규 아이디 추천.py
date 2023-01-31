#https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    ans = ''
    for i in new_id:
        if(i.isdigit() or i == '_' or i == '-'):
            ans += i
        if(i.isalpha()):
            ans += i.lower()
        if(i == '.'):
            if(len(ans) != 0):
                if(ans[-1] != '.'):
                    ans += i
    if(len(ans) > 0):
        if(ans[-1] == '.'):
            ans = ans[:-1]
    if(len(ans) == 0):
        ans = "aaa"
    if(len(ans) > 15):
        ans = ans[:15]
        if(ans[-1] == '.'):
            ans = ans[:-1]
    if(len(ans) == 1):
        ans += ans[-1]
        ans += ans[-1]
    if(len(ans) == 2):
        ans += ans[-1]

    
    return ans