#https://school.programmers.co.kr/learn/courses/30/lessons/87377

def cal_inter(a,b,e,c,d,f):
    x = b*f - e*d
    d = a*d - b*c
    y = e*c - a*f
    if(d != 0):
        if(abs(x) % abs(d) == 0 and abs(y) % abs(d) == 0):
            return (int(x/d),int(y/d))
    return (0.1,0.1)

def draw(intersec):
    minx = intersec[0][0]
    maxx = intersec[0][0]
    miny = intersec[0][1]
    maxy = intersec[0][1]
    for i in intersec:
        if(i[0]< minx):
            minx = i[0]
        elif(i[0]>maxx):
            maxx = i[0]
        if(i[1] < miny):
            miny = i[1]
        elif(i[1] > maxy):
            maxy = i[1]
    col = maxx-minx+1
    row = maxy-miny+1
    mat = [['.' for i in range(col)] for j in range(row)]
    for i in intersec:
        mat[maxy-i[1]][i[0]-minx] = '*'
    ret_list = []
    ret = ""
    for i in mat:
        for char in i:
            ret += char
        ret_list.append(ret)
        ret = ""
    return ret_list

def solution(line):
    answer = []
    intersec = []
    tem = (0,0)
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            tem = cal_inter(line[i][0],line[i][1],line[i][2],line[j][0],line[j][1],line[j][2])
            if(tem[0] != 0.1):
                if(tem not in intersec):
                    intersec.append(tem)
    answer = draw(intersec)
    return answer