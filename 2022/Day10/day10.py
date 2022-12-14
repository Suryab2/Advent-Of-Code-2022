file1 = open('input10.txt', 'r')
body=file1.read()
lines=body.splitlines()
x=1
cycle=0
tot=0
y=40
arr=[['?' for _ in range(40)] for _ in range(6)]
z=20
tot2=0
for line in lines:
    if line=="noop":
        cycle+=1
        tot2=cycle-1
        if(abs(x-(cycle%40))<=1):
            arr[tot2//40][cycle%40]=('#')
        else:
            arr[tot2//40][cycle%40]=' '
        if cycle in [20, 60, 100, 140, 180, 220]:
            tot+= x*cycle
        x=x
    else:
        s1,s2=line.split(" ")
        cycle+=1
        s2=int(s2)
        tot2=cycle-1
        if(abs(x-(tot2%40))<=1):
            arr[tot2//40][tot2%40]=('#')
        else:
            arr[tot2//40][tot2%40]=' '
        if cycle in [20, 60, 100, 140, 180, 220]:
            tot+= x*cycle
        cycle+=1
        tot2=cycle-1
        if(abs(x-(tot2%40))<=1):
            arr[tot2//40][tot2%40]=('#')
        else:
            arr[tot2//40][tot2%40]=' '
        if cycle in [20, 60, 100, 140, 180, 220]:
            tot+= x*cycle
        x+=s2
print(tot)
for i in range(6):
    print(''.join(arr[i]))
    
