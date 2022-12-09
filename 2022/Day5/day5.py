file1 = open('input5.txt', 'r')
body=file1.read()
lines=body.splitlines()
tot=0
a=['b','v','s','n','t','c','h','q']
b=['w','d','b','g']
c=['f','w','r','t','s','q','b']
d=['l','g','w','s','z','j','d','n']
e=['m','p','d','v','f']
f=['f','w','j']
g=['l','n','q','b','j','v']
h=['g','t','r','c','j','q','s','n']
i=['j','s','q','c','w','d','m']
x=[]
#m1=tomove,m3=from,m4=to
for line in lines:
    m1,m2=line.split('from')
    m3,m4=m2.split('to')
    m1,m3,m4=[int(x) for x in [m1,m3,m4]]
    # print(m3)
    if m3==1:
        for y in range(0,m1):
            x.append(a.pop())
        for q in range(m1-1,-1,-1):
            if(m4==1):
                a.append(x[q])
            elif(m4==2):
                b.append(x[q])
            elif(m4==3):
                c.append(x[q])
            elif(m4==4):
                d.append(x[q])
            elif(m4==5):
                e.append(x[q])
            elif(m4==6):
                f.append(x[q])
            elif(m4==7):
                g.append(x[q])
            elif(m4==8):
                h.append(x[q])
            elif(m4==9):
                i.append(x[q])
        x=[]
    elif m3==2:
        for y in range(0,m1):
            x.append(b.pop())
        for q in range(m1-1,-1,-1):
            if(m4==1):
                a.append(x[q])
            elif(m4==2):
                b.append(x[q])
            elif(m4==3):
                c.append(x[q])
            elif(m4==4):
                d.append(x[q])
            elif(m4==5):
                e.append(x[q])
            elif(m4==6):
                f.append(x[q])
            elif(m4==7):
                g.append(x[q])
            elif(m4==8):
                h.append(x[q])
            elif(m4==9):
                i.append(x[q])
        x=[]
    elif m3==4:
        for y in range(0,m1):
            x.append(d.pop())
        for q in range(m1-1,-1,-1):
            if(m4==1):
                a.append(x[q])
            elif(m4==2):
                b.append(x[q])
            elif(m4==3):
                c.append(x[q])
            elif(m4==4):
                d.append(x[q])
            elif(m4==5):
                e.append(x[q])
            elif(m4==6):
                f.append(x[q])
            elif(m4==7):
                g.append(x[q])
            elif(m4==8):
                h.append(x[q])
            elif(m4==9):
                i.append(x[q])
        x=[]
    elif m3==5:
        for y in range(0,m1-1):
            print(e)
            x.append(e.pop())
        for q in range(m1-1,-1,-1):
            if(m4==1):
                a.append(x[q])
            elif(m4==2):
                b.append(x[q])
            elif(m4==3):
                c.append(x[q])
            elif(m4==4):
                d.append(x[q])
            elif(m4==5):
                e.append(x[q])
            elif(m4==6):
                f.append(x[q])
            elif(m4==7):
                g.append(x[q])
            elif(m4==8):
                h.append(x[q])
            elif(m4==9):
                i.append(x[q])
        x=[]
    if m3==6:
        for y in range(0,m1):
            x.append(f.pop())
            # print(x)
            # break
        for q in range(m1-1,-1,-1):
            if(m4==1):
                a.append(x[q])
            elif(m4==2):
                b.append(x[q])
            elif(m4==3):
                c.append(x[q])
            elif(m4==4):
                d.append(x[q])
            elif(m4==5):
                e.append(x[q])
            elif(m4==6):
                f.append(x[q])
            elif(m4==7):
                g.append(x[q])
            elif(m4==8):
                h.append(x[q])
            elif(m4==9):
                i.append(x[q])
        x=[]
    elif m3==7:
        for y in range(0,m1):
            x.append(g.pop())
        for q in range(m1-1,-1,-1):
            if(m4==1):
                a.append(x[q])
            elif(m4==2):
                b.append(x[q])
            elif(m4==3):
                c.append(x[q])
            elif(m4==4):
                d.append(x[q])
            elif(m4==5):
                e.append(x[q])
            elif(m4==6):
                f.append(x[q])
            elif(m4==7):
                g.append(x[q])
            elif(m4==8):
                h.append(x[q])
            elif(m4==9):
                i.append(x[q])
        x=[]
    elif m3==8:
        for y in range(0,m1):
            x.append(h.pop())
        for q in range(m1-1,-1,-1):
            if(m4==1):
                a.append(x[q])
            elif(m4==2):
                b.append(x[q])
            elif(m4==3):
                c.append(x[q])
            elif(m4==4):
                d.append(x[q])
            elif(m4==5):
                e.append(x[q])
            elif(m4==6):
                f.append(x[q])
            elif(m4==7):
                g.append(x[q])
            elif(m4==8):
                h.append(x[q])
            elif(m4==9):
                i.append(x[q])
        x=[]
    elif m3==9:
        for y in range(0,m1):
            x.append(i.pop())
        for q in range(m1-1,-1,-1):
            if(m4==1):
                a.append(x[q])
            elif(m4==2):
                b.append(x[q])
            elif(m4==3):
                c.append(x[q])
            elif(m4==4):
                d.append(x[q])
            elif(m4==5):
                e.append(x[q])
            elif(m4==6):
                f.append(x[q])
            elif(m4==7):
                g.append(x[q])
            elif(m4==8):
                h.append(x[q])
            elif(m4==9):
                i.append(x[q])
        x=[]
    # break
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)



    