from collections import defaultdict
file1 = open('input7.txt', 'r')
body=file1.read()
lines=body.splitlines()
# struct=defaultdict(defaultdict)
# struct['/']=defaultdict()
# CURR='/'

class Node:
    def __init__(self,name,size=0):
        self.name=name
        self.size=size
        self.children=[]
        self.parent=None
Nodes=Node('/')
curr=Nodes
count=0
for line in lines: 
    if line.startswith('$'):
        s1=line.split()
        s2=s1[1]
        if s2=='cd':
            s3=s1[2]
            if s3=='..':
                curr=curr.parent
                pass
            else:
                n=Node(s3)
                n.parent=curr 
                curr.children.append(n)
                curr=n
            count+=1
        elif s2=='ls':
            count+=1
            continue
    else:
        s1=line.split()
        if s1[0]=='dir':
            pass
        else:
            siz,name=s1[0],s1[1]
            curr.children.append(Node(name,int(siz)))
        count+=1
seen=set()
total=0
tot=0
sizes={}
def dfs(node,size=0):
    if not node.children:
        return node.size
    tot=0
    for n in node.children:
        tot+=dfs(n)
    seen.add(node)
    if tot<100000:
        global total
        total+=tot
    return tot
dfs(Nodes)
print(total)
tot=0
def dfs2(node,size=0):
    if not node.children:
        return node.size
    tot=0
    for n in node.children:
        tot+=dfs2(n)
    sizes[node.name]=tot
    return tot
dfs2(Nodes)
tot_available=70000000
tot_needed=30000000
used=sizes['/']
unused=tot_available-used
for size in sorted(sizes.values()):
    if unused+size>=tot_needed:
        print(size)
        break











