file1 = open('input4.txt', 'r')
body=file1.read()
lines=body.splitlines()
tot=0
for line in lines:
    str1,str2=line.split(',')
    num1,num2=str1.split('-')
    num3,num4=str2.split('-')
    num1,num2,num3,num4=[int(x) for x in [num1,num2,num3,num4]]
    #first part answer
    # if num1<=num3 and num4<=num2 or num3<=num1 and num2<=num4:
        # tot+=1
    #second part answer
    if(num1<=num3 and num2>=num3 or num3<=num1 and num4>=num1):
        tot+=1
print(tot)