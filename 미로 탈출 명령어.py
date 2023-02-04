#https://school.programmers.co.kr/learn/courses/30/lessons/150365

def can_go(n,m,x,y,r,c,wx,wy,k):
    if(wx != 0):
        if(x + wx > n or x + wx <= 0):
            return False
        if(abs(x + wx - r) + abs(y - c) > k):
            return False
    else:
        if(y + wy > m or y + wy <= 0):
            return False
        if(abs(x - r) + abs(y + wy - c) > k):
            return False
    return True
def solution(n, m, x, y, r, c, k):
    answer = ''
    now_x = x
    now_y = y
    if(((x - r) + (y-c) - k) %2 == 1):
        #return 'impossible'
    while(k>0):
        if(can_go(n,m,now_x,now_y,r,c,1,0,k)):
            answer += 'd'
            now_x += 1
        elif(can_go(n,m,now_x,now_y,r,c,0,-1,k)):
            answer += 'l'
            now_y -= 1
        elif(can_go(n,m,now_x,now_y,r,c,0,1,k)):
            answer += 'r'
            now_y += 1
        elif(can_go(n,m,now_x,now_y,r,c,-1,0,k)):
            answer += 'u'
            now_x -= 1
        k -= 1

    return answer

print(solution(3,3,1,2,3,3,4))