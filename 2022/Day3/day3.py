file1 = open('input3.txt', 'r')
body=file1.read()
lines=body.splitlines()

firsthalf=[]
secondhalf=[]
tot=0
for line in lines:
    firsthalf=[]
    secondhalf=[]
    for k in range(0,len(line)//2):
        firsthalf.append(line[k])
    for z in range(len(line)//2,len(line)):
        secondhalf.append(line[z])
    for z in firsthalf:
        if(secondhalf.__contains__(z)):
            if 'a'<=z<='z':
                tot+=ord(z)-ord('a')+1
            else:
                tot+=ord(z)-ord('A')+1+26
            break
a=[]
total=0
for line in lines:
    a.append(line)
print(a)
for i in range(0,len(a),3):
    out=set(a[i]) & set(a[i+1]) & set(a[i+2])
    if 'a'<=''.join(out)<='z':
        total+=ord(''.join(out))-ord('a')+1
    else:
        total+=ord(''.join(out))-ord('A')+1+26
print(total)
