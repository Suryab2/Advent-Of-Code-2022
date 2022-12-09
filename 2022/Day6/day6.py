file1 = open('input6.txt', 'r')
body=file1.read()
s=[]
m=[]

lines=body.splitlines()
i=0
z=0
count=0
# print(len(s))
for line in lines:
    m.append(line)
for k in m:
    if(len(s)==7 or len(s)==2 or len(s)==4 or len(s)==3):
        count+=1
        s=[]
        print(count)
    else:
        s=[]
    print('this',k)
    s1,s2= k.split('|')
    for y in s2:
        if(y==" "):
            if(len(s)==2):
                count+=1
                print(count)
            elif(len(s)==3):
                count+=1
                print(count)
            elif(len(s)==4):
                count+=1
                print(count)
            elif(len(s)==5):
                count+=1
                print(count)
            elif(len(s)==5):
                count+=1
                print(count)
            elif(len(s)==5):
                count+=1
                print(count)
            elif(len(s)==5):
                count+=1
                print(count)
            elif(len(s)==5):
                count+=1
                print(count)
            s=[]
        else:
            s.append(y)
            print(s)
print(s1)
print(s)
if(len(s)==1 or len(s)==2 or len(s)==4 or len(s)==3):
    print(count+1)
else:
    print(count)
# for z in range(len(m)):
#     if(len(s)==14):
#         break
#     elif(len(m)-z>=14):
#         s.append(m[z])
#         s.append(m[z+1])
#         s.append(m[z+2])
#         s.append(m[z+3])
#         s.append(m[z+4])
#         s.append(m[z+5])
#         s.append(m[z+6])
#         s.append(m[z+7])
#         s.append(m[z+8])
#         s.append(m[z+9])
#         s.append(m[z+10])
#         s.append(m[z+11])
#         s.append(m[z+12])
#         s.append(m[z+13])
#         myset=set(s)
#         if(len(myset)!=14):
#             s=[]
#         i+=1
# print(i+13)
    
        