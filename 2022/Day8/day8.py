# import numpy as np
file1 = open('input8.txt', 'r')
body=file1.read()
lines=body.splitlines()
a=[]
matrix=[]
for line in lines:
    a=[]
    for k in line:
        a.append(k)
    matrix.append(a)
greater=0
edge=392
count=0
val=False
# for i in range(0,99):
#     # val=False
#     for j in range(0,99):
#         x=y=m=l=0
#         greater=matrix[i][j]
#         for z in range(j-1,-1,-1):
#             x+=1
#             if(matrix[i][z]>=greater):
#                 break
#         for z in range(j+1,99):
#             y+=1
#             if(matrix[i][z]>=greater):
#                 break
#             # print(i,z)
#         for z in range(i+1,99):
#              m+=1
#              if(matrix[z][j]>=greater):
#                 break
#         for z in range(i-1,-1,-1):
#             l+=1
#             if(matrix[z][j]>=greater):
#                 break
#         count=max(count,x*y*m*l)
# print(count)
sum=0
for i in range(1,98):
    for j in range(1,98):
        greater=matrix[i][j]
        for z in range(j-1,-1,-1):
            if(matrix[i][z]>=greater):
                greater=matrix[i][z]
        if(greater==matrix[i][j]):
            sum+=1
            continue
        for z in range(j+1,99):
            if(matrix[i][z]>=greater):
                greater=matrix[i][z]
        if(greater==matrix[i][j]):
            sum+=1
            continue
            # print(i,z)
        for z in range(i+1,99):
            if(matrix[z][j]>=greater):
                greater=matrix[z][j]
        if(greater==matrix[i][j]):
            sum+=1
            continue
        for z in range(i-1,-1,-1):
            if(matrix[z][j]>=greater):
                greater=matrix[z][j]
        if(greater==matrix[i][j]):
            sum+=1
            continue
print(sum)
    
# import numpy as np
# file1 = open('input8.txt', 'r')
# body=file1.read()
# lines=body.splitlines()
# a=[]
# matrix=[]
# for line in lines:
#     a=[]
#     for k in line:
#         a.append(k)
#     matrix.append(a)
# greater=0
# edge=392
# count=0
# val=False
# for i in range(0,99):
#     # val=False
#     for j in range(0,99):
#         s=matrix[i][j]

# print(count+392)




    