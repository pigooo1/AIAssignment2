from IO import *

from UniformCostSearch import *
from GreedyBestFirst import *
from Astar import*
from PriorityQueue import *
from Node import *
from scaleNode import *


def runUCS(fileName,goalState1,goalState2,scale):
    puzzles = readFile(fileName)
    i=0
    success=0
    solutionPathLength=[]
    searchPathLength=[]
    visitCost=[] # Only for success
    createdCost=[]
    excutionTime=[]
    for x in puzzles:
        if(scale==False):
            N1=Node(str(x),None,0,0,0,"gn",0,0)
        else:
            N1=scaleNode(str(x),None,0,0,0,"gn",0,'A')
        openList=PriorityQueue(N1)
        closedList=[]
        goal1=goalState1
        goal2=goalState2
        if(scale==False):
            result=uniformCostSearch(openList,closedList,goal1,goal2,60)
        else:
            result = uniformCostSearch(openList, closedList, goal1, goal2, 99999)
        if(scale==False):
            outputFile(str(i)+"_ucs_",result[0],result[1])
        else:
            outputFile(str(i) + "_ucs_scale_", result[0], result[1])
        if(result[2]==True):
            success+=1
            solutionPathLength.append(result[3])
            searchPathLength.append(result[4])
            visitCost.append(result[5])
            createdCost.append(result[6])
            excutionTime.append(result[7])
        i+=1
    if (scale == False):
        generateAnalysis("UCS", [i, success, solutionPathLength, searchPathLength, visitCost, createdCost, excutionTime])
    else:
        generateAnalysis("UCS_scale",[i, success, solutionPathLength, searchPathLength, visitCost, createdCost, excutionTime])

def runGBFS(heuristics,fileName,goalState1,goalState2,scale):
    puzzles = readFile(fileName)
    i=0
    success=0
    solutionPathLength=[]
    searchPathLength=[]
    visitCost=[] # Only for success
    createdCost=[]
    excutionTime=[]
    for x in puzzles:
        if(scale==False):
            N1=Node(str(x),None,0,0,0,"hn",0,0)
        else:
            N1=scaleNode(str(x),None,0,0,0,"hn",0,'A')
        openList=PriorityQueue(N1)
        closedList=[]
        goal1=goalState1
        goal2=goalState2
        if(scale==False):
            result=greedyBestFirstSearch(openList,closedList,goal1,goal2,heuristics,60)
        else:
            result = greedyBestFirstSearch(openList, closedList, goal1, goal2, heuristics, 99999)
        if(scale==False):
            outputFile(str(i)+"_gbfs_"+heuristics+"_",result[0],result[1])
        else:
            outputFile(str(i) + "_gbfs_scale_" + heuristics + "_", result[0], result[1])
        if(result[2]==True):
            success+=1
            solutionPathLength.append(result[3])
            searchPathLength.append(result[4])
            visitCost.append(result[5])
            createdCost.append(result[6])
            excutionTime.append(result[7])
        i+=1
    if (scale == False):
        generateAnalysis("gbfs_"+heuristics, [i, success, solutionPathLength, searchPathLength, visitCost, createdCost, excutionTime])
    else:
        generateAnalysis("gbfs_scale" + heuristics,[i, success, solutionPathLength, searchPathLength, visitCost, createdCost, excutionTime])

def runAstar(heuristics,fileName,goalState1,goalState2,scale):
    puzzles = readFile(fileName)
    i=0
    success=0
    solutionPathLength=[]
    searchPathLength=[]
    visitCost=[] # Only for success
    createdCost=[]
    excutionTime=[]
    for x in puzzles:
        if (scale == False):
            N1 = Node(str(x), None, 0, 0, 0, "fn", 0, 0)
        else:
            N1 = scaleNode(str(x), None, 0, 0, 0, "fn", 0, 'A')
        openList=PriorityQueue(N1)
        closedList=[]
        goal1=goalState1
        goal2=goalState2
        if (scale == False):
            result=aStarSearch(openList,closedList,goal1,goal2,heuristics,60)
        else:
            result = aStarSearch(openList, closedList, goal1, goal2, heuristics, 3600)
        if(scale==False):
            outputFile(str(i)+"_astar_"+heuristics+"_",result[0],result[1])
        else:
            outputFile(str(i) + "_astar_scale" + heuristics + "_", result[0], result[1])
        if(result[2]==True):
            success+=1
            solutionPathLength.append(result[3])
            searchPathLength.append(result[4])
            visitCost.append(result[5])
            createdCost.append(result[6])
            excutionTime.append(result[7])
        i+=1
    if (scale == False):
        generateAnalysis("aStar_"+heuristics, [i, success, solutionPathLength, searchPathLength, visitCost, createdCost, excutionTime])
    else:
        generateAnalysis("aStar_scale_" + heuristics,[i, success, solutionPathLength, searchPathLength, visitCost, createdCost, excutionTime])



#generatePuzzles()
#runUCS("randomPuzzles.txt","12345670","13572460",False)
#runGBFS("h1","randomPuzzles.txt","12345670","13572460",False)
#runGBFS("h2","randomPuzzles.txt","12345670","13572460",False)
runAstar("h1","randomPuzzles.txt","12345670","13572460",False)
runAstar("h2","randomPuzzles.txt","12345670","13572460",False)

#generateScaledPuzzles()
#runUCS("randomScaledPuzzles.txt","BCDEFGHIJKLA","BEHKCFILDGJA",True)
#runGBFS("h1","randomScaledPuzzles.txt","BCDEFGHIJKLA","BEHKCFILDGJA",True)
#runGBFS("scaleh2","randomScaledPuzzles.txt","BCDEFGHIJKLA","BEHKCFILDGJA",True)
#runAstar("scaleh2","randomScaledPuzzles.txt","BCDEFGHIJKLA","BEHKCFILDGJA",True)