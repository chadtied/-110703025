import networkx as Net
import matplotlib.pyplot as plt
from operator import attrgetter
import random

Map= Net.Graph()
path= [[0]*1000 for i in range(1000)]
class short:
    def __init__(self, parent, itself, cost):
        self.parent= parent
        self.itself= itself
        self.cost= cost
short_path= []
list= []
start= random.randrange(1000)

for i in range(0,1000):
    if i!= start:
        short_path.append(short(-1,i,1000))
    else:
        short_path.append(short(start,start,0))
        
    for k in range(0,1000):
        if i+1== k or k+1== i:
            path[i][k]= 1
        else:
            path[i][k]= 0
path[0][999]= 1
path[999][0]= 1

count= 0
while count< 100:
    row= random.randrange(1000)
    col= random.randrange(1000)
    if path[row][col]!= 1 and path[col][row]!= 1:
        path[row][col]= 1
        path[col][row]= 1
        count+= 1


'''for to in range(0,1000):
    if path[start][to]!= 0:
        short_path[to].parent= start
        short_path[to].itself= to 
        short_path[to].cost= path[start][to]'''
                
short_path= sorted(short_path, key = attrgetter('cost'))


while len(short_path)!= 0:
    start= short_path[0].itself
    for to in range(0,1000):
        if path[start][to]!= 0 and (short_path[0].parent!= to):
            #print(start, to)
            
            for k in range(0,len(short_path)):
                if short_path[k].itself== to:
                    if short_path[k].cost> path[start][to]+ short_path[0].cost:
                        short_path[k].parent= start
                        #print('\n')
                        short_path[k].cost= path[start][to]+ short_path[0].cost
                        break

    list.append(short_path[0])
    '''for i in range(0,len(short_path)):
        print(short_path[i].parent, short_path[i].itself, short_path[i].cost)
    print('\n')'''
    
    short_path.pop(0)
    short_path= sorted(short_path, key = attrgetter('cost'))
    
sum= 0

for i in range(0,len(list)):
    sum+= list[i].cost
print(sum/1000)


            
'''for i in range(0,len(short_path)):
    for ptr in range(0,path[short_path[i].to]):
        if path[short_path[i].to]!= 0:
'''        

        

'''for i in range(0,999):
    Map.add_edges_from([(i,i+1)])
Map.add_edges_from([(999,1)])
Net.draw(Map, node_size= 0.5, node_shape= 'd', pos= Net.circular_layout(Map))

#with_labels= True

plt.show()
'''
