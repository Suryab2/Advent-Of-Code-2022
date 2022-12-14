import sys
file1 = sys.argv[1] if len(sys.argv)>1 else 'input13.txt'
body=open(file1).read().strip()
lines = [x for x in body.split('\n')]
def compare(left,right):
    if isinstance(left, int) and isinstance(right,int):
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1
    elif isinstance(left, list) and isinstance(right, list):
        i = 0
        while i<len(left) and i<len(right):
            c = compare(left[i], right[i])
            if c==-1:
                return -1
            if c==1:
                return 1
            i += 1
        if i==len(left) and i<len(right):
            return -1
        elif i==len(right) and i<len(left):
            return 1
        else:
            return 0
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    else:
        return compare(left, [right])
count=0
packets=[]
for i,group in enumerate(body.split('\n\n')):
    left,right = group.split('\n')
    left = eval(left)
    right = eval(right)
    packets.append(left)
    packets.append(right)
    if compare(left,right)== -1:
        count+=1+i
    elif compare(left,right)==1:
        pass
packets.append([[2]])
packets.append([[6]])
from functools import cmp_to_key
packets = sorted(packets, key=cmp_to_key(lambda left,right: compare(left,right)))
part2 = 1
for i,p in enumerate(packets):
    if p==[[2]] or p==[[6]]:
        part2 *= i+1
print(part2)
    
print(count) 


        
