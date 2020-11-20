from PriorityQueue import *
from Node import *
from heuristics import *
from IO import *
import time


def greedyBestFirstSearch(openList, closedList, goal1, goal2, heuristics,mytime):
        startTime=time.time()
        result=[]
        searchPath=''
        searchLength=0
        visit=0
        created=0
        while(time.time()-startTime<=mytime):
            currentNode=openList.pop()
            searchPath=searchPath+currentNode.toSearchString()+"\n"
            searchLength += currentNode.moveCost
            visit+=1
            if (currentNode.c_state==goal1 or currentNode.c_state==goal2):
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
                if(not any(y.c_state == x.c_state for y in closedList)):
                    if (heuristics=='h1'):
                        h1(x,goal1,goal2)
                    elif (heuristics=='h2'):
                        h2(x,goal1,goal2)
                    elif (heuristics=='scaleh2'):
                        scaleh2(x,goal1,goal2)
                    openList.push(x)
            closedList.append(currentNode)
        result.append("no solution") #solutionPath
        result.append("no solution") #searchPath
        result.append(False) #no solution
        return (result)
