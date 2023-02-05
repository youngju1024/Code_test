#https://school.programmers.co.kr/learn/courses/30/lessons/155651

def solution(book_time):
    timetable = [0 for _ in range(24*60+1)]
    for t in book_time:
        tem = t[0].split(":")
        tem2 = t[1].split(":")
        start = int(tem[0])*60+int(tem[1])
        end = int(tem2[0])*60+int(tem2[1])
        timetable[start] += 1
        if(end+10 < 24*60):
            timetable[end+10] -= 1
    t = 0
    for i in range(len(timetable)):
        t += timetable[i] 
        timetable[i] = t
        
    return max(timetable)