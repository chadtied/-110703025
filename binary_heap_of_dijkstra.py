import random

class edge:
    def __init__(self, parent, itself, cost):
        self.parent= parent
        self.itself= itself
        self.cost= cost
def Print(output):
    for i in range(0,len(output)):
        print(output[i].parent, output[i].itself, output[i].cost)
    print('\n')
        
def insert(short_path, obj):
    short_path.append(obj)
    length= len(short_path)
    while length> 1:
        if short_path[int(length/2)-1].cost> short_path[length-1].cost:
            tmp= short_path[length-1]
            short_path[length-1]= short_path[int(length/2)-1]
            short_path[int(length/2)-1]= tmp
            length= int(length/2)
        else:
            break
def ExtractMin(short_path, list):
    list.append(short_path[0])
    short_path[0]= short_path[len(short_path)-1]
    short_path.pop(len(short_path)-1)
    ptr= 1
    
    while True:
        flag= 0
        if ((2*ptr-1< len(short_path) and short_path[ptr-1].cost> short_path[2*ptr-1].cost) and (2*ptr< len(short_path) and short_path[ptr-1].cost> short_path[2*ptr].cost)):
            if short_path[2*ptr-1].cost< short_path[2*ptr].cost:
                flag= 1
            else:
                flag= 2
        elif 2*ptr-1< len(short_path) and short_path[ptr-1].cost> short_path[2*ptr-1].cost:
            flag= 1
        elif 2*ptr< len(short_path) and short_path[ptr-1].cost> short_path[2*ptr].cost:
            flag= 2
        
        if (flag== 1):
            tmp= short_path[ptr-1]
            short_path[ptr-1]= short_path[ptr*2-1]
            short_path[2*ptr-1]= tmp
            ptr= 2*ptr
        elif(flag== 2):
            tmp= short_path[ptr-1]
            short_path[ptr-1]= short_path[ptr*2]
            short_path[2*ptr]= tmp
            ptr= 2*ptr+1
        else:
            break
    
def decreaseKey(short_path, target):
    ptr= target+ 1
    while True:
        if short_path[ptr-1].cost< short_path[int(ptr/2)-1].cost:
            tmp= short_path[ptr-1]
            short_path[ptr-1]= short_path[int(ptr/2)-1]
            short_path[int(ptr/2)-1]= tmp
            ptr= int(ptr/2)
        else:
            break
    

start= random.randrange(1000)
short_path= []
list= []

weight= [[0]*1000 for i in range(1000)]

for row in range(1000):
    for col in range(1000):
        if row== col +1 or row+ 1== col:
            weight[row][col]= 1 
        else:
            weight[row][col]= 0
weight[0][999]= 1
weight[999][0]= 1

count= 0
while count< 100:
    row= random.randrange(1000)
    col= random.randrange(1000)
    if row!= col and weight[row][col]!= 1 and weight[col][row]!= 1:
        weight[row][col]= 1
        weight[col][row]= 1
        count+= 1



for i in range(0,1000):
    if i== start:
        insert(short_path, edge(start, start, 0))
    else:
         insert(short_path, edge(-1, i, 1000))

#Print(short_path)
         

while len(short_path)!= 0:
    start= short_path[0].itself
    for it in range(0,len(weight[start])):
        flag= True
        if weight[start][it]!= 0 and it!= short_path[0].parent:
            target= 0

            for i in range(0,len(short_path)):
                if short_path[i].itself== it:
                    target= i
                    break
                elif i== len(short_path)-1:
                    flag= False
                
            if flag== True and short_path[0].cost+ weight[start][it]< short_path[target].cost:
                short_path[target].cost= short_path[0].cost+ weight[start][it]
                short_path[target].parent= start
                decreaseKey(short_path, target)
    #Print(short_path)
    ExtractMin(short_path, list)
    

sum= 0

for i in range(0,len(list)):
    sum+= list[i].cost
    #Print(short_path)
print(sum/1000)             
