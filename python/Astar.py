from PriorityQueue import *
from Node import *
from heuristics import *
from IO import *
import time


def aStarSearch(openList, closedList, goal1, goal2, heuristics,mytime):
        startTime=time.time()
        result=[]
        searchPath=''
        searchLength=0
        visit=0
        created=0

        while(time.time()-startTime<=mytime):
            currentNode=openList.pop()
            #print(currentNode.toSearchString())
            searchPath=searchPath+currentNode.toSearchString()+"\n"
            searchLength += currentNode.moveCost
            visit+=1
            if (currentNode.c_state==goal1 or currentNode.c_state==goal2):#success
                result.append(backTrack(currentNode,closedList)+"\n"+f"{currentNode.gn} {time.time()-startTime}")
                result.append(searchPath)
                result.append(True)
                result.append(currentNode.gn)
                result.append(searchLength)
                result.append(visit)
                result.append(created)
                result.append(time.time()-startTime)
                return (result)
            currentNode.generateNextSteps()
            successors=currentNode.generateSuccessors()
            for x in successors:
                created+=1#shouldn't add searchLength here, cause if we reach a node in closed list ,we don't care it cost
                if (heuristics == 'h1'):
                    h1(x, goal1, goal2)
                    x.fn=x.hn+x.gn
                elif (heuristics == 'h2'):
                    h2(x, goal1, goal2)
                    x.fn=x.hn+x.gn
                elif (heuristics == 'scaleh2'):
                    scaleh2(x, goal1, goal2)
                    x.fn=x.hn+x.gn
                for y in list(closedList):
                    if(y.c_state==x.c_state):
                        if(x.fn<y.fn ):
                            closedList.remove(y) #x fn is smaller than closed list
                if(not any(y.c_state == x.c_state for y in closedList)): # The closed is not delete
                    openList.push(x)
            closedList.append(currentNode)
        result.append("no solution") #solutionPath
        result.append("no solution") #searchPath
        result.append(False) #no solution
        return (result)