file1 = open('input14.txt', 'r')
body=file1.read()
lines=body.splitlines()
matrix=set()
for line in lines:
    prev=None
    for coordinates in line.split('->'):
        x,y=coordinates.split(',')
        x,y=int(x),int(y)
        if prev is not None:
            xx=x-prev[0]
            yy=y-prev[1]
            length=max(abs(xx),abs(yy))
            for i in range(length+1):
                dx=prev[0]+i*(1 if xx>0 else(-1 if xx<0 else 0))
                dy=prev[1]+i*(1 if yy>0 else(-1 if yy<0 else 0))
                matrix.add((dx,dy))
        prev=(x,y)
# print(len(matrix))
floor=2+(max(r[1] for r in matrix))
lo_x = min(r[0] for r in matrix)-1000
hi_x = max(r[0] for r in matrix)+1000
for x in range(lo_x, hi_x):
    matrix.add((x,floor))
val=True
for t in range(100000):
    rock=(500,0)
    # print(t)
    while True:
        if rock[1]+1>=floor and val==True:
            print(t)
            val= False
        elif (rock[0],rock[1]+1)not in matrix:
            rock=(rock[0],rock[1]+1)
        elif (rock[0]-1,rock[1]+1) not in matrix:
            rock=(rock[0]-1,rock[1]+1)
        elif(rock[0]+1,rock[1]+1) not in matrix:
            rock=(rock[0]+1,rock[1]+1)
        else:
            # print('breaking')
            break
    if rock==(500,0):
        print(t+1)
        break
    matrix.add(rock)
