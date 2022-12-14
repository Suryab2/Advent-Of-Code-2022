file1 = open('input9.txt', 'r')
body=file1.read()
lines=body.splitlines()
col_path={'L':0,'U':-1,'R':0,'D':1}
row_path={'L':-1,'U':0,'R':1,'D':0}  
H=(0,0)
T=[(0,0) for i in range(9)]
T1=(0,0)

def findT(H,T):
    col=(H[0]-T[0])
    row=(H[1]-T[1])
    if abs(row)<=1 and abs(col)<=1:
        pass
    elif abs(row)>=2 and abs(col)>=2:
        if T[0]<H[0]:
            if T[1]<H[1]:
                T=(H[0]-1,H[1]-1)
            else:
                T=(H[0]-1,H[1]+1)
        else:
            if T[1]<H[1]:
                T=(H[0]+1,H[1]-1)
            else:
                T=(H[0]+1,H[1]+1)
    elif abs(col)>=2:
        if T[0]<H[0]:
            T=(H[0]-1,H[1])
        else:
            T=(H[0]+1,H[1])
    elif abs(row)>=2:
       if T[1]<H[1]:
            T=(H[0],H[1]-1)
       else:
            T=(H[0],H[1]+1)
    return T

#first answer
traversed1=set()
for line in lines:
    s1,s2=line.split(' ')
    # print(s1,s2)
    s2=int(s2)
    for z in range(s2):
        traversed1.add(T1)
        H=(H[0]+col_path[s1],H[1]+row_path[s1])
        T1=findT(H,T1)
    traversed1.add(T1)

#second answer
H=(0,0)
traversed2=set()
for line in lines:
    s1,s2=line.split(' ')
    # print(s1,s2)
    s2=int(s2)
    for z in range(s2):
        traversed2.add(T[8])
        H=(H[0]+col_path[s1],H[1]+row_path[s1])
        T[0]=findT(H,T[0])
        for i in range(1,9):
            T[i]=findT(T[i-1],T[i])
        traversed2.add(T[8])



print(len(traversed1))
print(len(traversed2))






