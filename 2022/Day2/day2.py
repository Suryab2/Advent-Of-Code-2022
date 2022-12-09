file1 = open('input2.txt', 'r')
body=file1.read()
lines=body.splitlines()
total1=0
total2=0
for line in lines:
    if(line=="A X"):
        total1=total1+1+3
    elif(line=="A Y"):
        total1=total1+2+6
    elif(line=="A Z"):
        total1=total1+3+0
    elif(line=="B X"):
        total1=total1+1+0
    elif(line=="B Y"):
        total1=total1+2+3
    elif(line=="B Z"):
        total1=total1+3+6
    elif(line=="C X"):
        total1=total1+1+6
    elif(line=="C Y"):
        total1=total1+2+0
    elif(line=="C Z"):
        total1=total1+3+3
print(total1)


for line in lines:
    if(line=="A X"):
        total2=total2+3+0
    elif(line=="A Y"):
        total2=total2+1+3
    elif(line=="A Z"):
        total2=total2+2+6
    elif(line=="B X"):
        total2=total2+1+0
    elif(line=="B Y"):
        total2=total2+2+3
    elif(line=="B Z"):
        total2=total2+3+6
    elif(line=="C X"):
        total2=total2+2+0
    elif(line=="C Y"):
        total2=total2+3+3
    elif(line=="C Z"):
        total2=total2+1+6
print(total2)