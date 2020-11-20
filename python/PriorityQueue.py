from Node import *
import random
import heapq

class PriorityQueue:
    def __init__(self, initialState:Node):
        self.initialState=initialState
        self.priorityQueue=[initialState]

    def pop(self):
        return heapq.heappop(self.priorityQueue)

    def push(self,item):
        if(self.containReplace(item)==False):
            heapq.heappush(self.priorityQueue,item)

    def containReplace(self,item):
        for x in list(self.priorityQueue):
            if(x.c_state==item.c_state):
                if(x.decision=='gn'):
                    if(x.gn>item.gn):
                        #print(f"found!,remove {x.toString()}")
                        #print(f"      ,replace {item.toString()}")
                        self.priorityQueue.remove(x)
                        self.priorityQueue.append(item)
                        heapq.heapify(self.priorityQueue)
                        return True
                if(x.decision=='hn'):
                    if(x.hn>item.hn):
                        #print("hnreplacement work“)
                        #print(f"found!,remove {x.toString()}")
                        #print(f"      ,replace {item.toString()}")
                        self.priorityQueue.remove(x)
                        self.priorityQueue.append(item)
                        heapq.heapify(self.priorityQueue)
                        return True
                if(x.decision=='fn'):
                    if(x.fn>item.fn):
                        #print("hnreplacement work“)
                        #print(f"found!,remove {x.toString()}")
                        #print(f"      ,replace {item.toString()}")
                        self.priorityQueue.remove(x)
                        self.priorityQueue.append(item)
                        heapq.heapify(self.priorityQueue)
                        return True
        return False

    def toString(self):
        result=''
        for x in self.priorityQueue:
            result += x.toString()+"\n"
        return result

    def toSortedString(self):
        result=''
        temp=list(self.priorityQueue)
        for x in range(len(temp)):
            result += heapq.heappop(temp).toString()+"\n"
        return result

# N1=Node("12304567",None,0,"gn")
# myList=PriorityQueue("gn",N1)
# N1.generateNextSteps()
# successor=N1.generateSuccessors()
#
# for x in successor:
#     heapq.heappush(myList.priorityQueue,x)
#
# #myheap.sort(key=lambda x:x.gn)
#
#
# myList.push(Node("12384560","123",0,"gn"))
#
# print(myList.toString())
# print(myList.toSortedString())