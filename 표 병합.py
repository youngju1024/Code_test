#https://school.programmers.co.kr/learn/courses/30/lessons/150366

def find_root(a,b,parent):
    while(parent[a][b] != (a,b)):
        return find_root(parent[a][b][0],parent[a][b][1],parent)
    return (a,b)

def solution(commands):
    answer = []
    table = [["EMPTY" for _ in range(51)] for _ in range(51)]
    parent = [[(i,j) for j in range(51)] for i in range(51)]
    for t in commands:
        tem = t.split(' ')
        if(tem[0] == "UPDATE"):
            if(len(tem) == 4):
                root = find_root(int(tem[1]),int(tem[2]),parent)
                table[root[0]][root[1]] = tem[3]
            else:
                for i in range(1,51):
                    for j in range(1,51):
                        if(table[i][j] == tem[1]):
                            table[i][j] = tem[2]
        elif(tem[0] == "MERGE"):
            root1 = find_root(int(tem[1]),int(tem[2]),parent)
            root2 = find_root(int(tem[3]),int(tem[4]),parent)
            parent[root2[0]][root2[1]] = root1
            if(table[root1[0]][root1[1]] == "EMPTY"):
                table[root1[0]][root1[1]] = table[root2[0]][root2[1]]
        elif(tem[0] == "UNMERGE"):
            root = find_root(int(tem[1]),int(tem[2]),parent)
            save = table[root[0]][root[1]]
            change = []
            for i in range(1,51):
                for j in range(1,51):
                    if(find_root(i,j,parent) == root):
                        change.append([i,j])
            for i in change:
                table[i[0]][i[1]] = "EMPTY"
                parent[i[0]][i[1]] = (i[0],i[1])
            table[int(tem[1])][int(tem[2])] = save
        elif(tem[0] == "PRINT"):
            root = find_root(int(tem[1]),int(tem[2]),parent)
            answer.append(table[root[0]][root[1]])
    return answer