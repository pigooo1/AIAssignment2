import random

def readFile(fileName):
    input = open("input/"+fileName, "r")
    inputPuzzles = []
    for line in input:
      result = line.replace(' ','')
      result = result.replace('\n', '')
      inputPuzzles.append(result)
    return inputPuzzles

def outputFile(fileName,solution,search):
    solutionoutput= open("output/"+fileName+"_solution.txt", "w")
    solutionoutput.write(solution)
    solutionoutput= open("output/"+fileName+"_search.txt", "w")
    solutionoutput.write(search)

def generateAnalysis(searchMethod,data):

    result=''
    total=data[1]
    totalSolutionPathLength=0
    totalSearchPathLength=0
    totalVisitCost=0
    totalCreatedCost=0
    totalExcutionTime=0

    for x in data[2]:
        totalSolutionPathLength+=x
    for x in data[3]:
        totalSearchPathLength+=x
    for x in data[4]:
        totalVisitCost+=x
    for x in data[5]:
        totalCreatedCost+=x
    for x in data[6]:
        totalExcutionTime+=x
    result+='The length of path,cost,excution time are based on successful search'+'\n'
    result+=f'1. Solution Path Length      Average:{totalSolutionPathLength/total}   total:{totalSolutionPathLength}'+'\n'
    result+=f'   Search Path Length        Average:{totalSearchPathLength/total}     total:{totalSearchPathLength}'+'\n'
    result+=f'2. There are {data[0]-data[1]} no solution in {data[0]} searches'+'\n'
    result+=f'3. Node Created Cost     Average:{totalCreatedCost/total}   total:{totalCreatedCost}'+'\n'
    result+=f'   Node Visited Cost     Average:{totalVisitCost / total}   total:{totalVisitCost}' + '\n'
    result+=f'   Execution Time        Average:{totalExcutionTime/total}  total:{totalExcutionTime}'
    solutionoutput= open("output/"+searchMethod+"_analysis.txt", "w")
    solutionoutput.write(result)


def generatePuzzles():
    initial = [0, 1, 2, 3, 4, 5, 6, 7]
    result = ''
    for x in range(50):
        random.shuffle(initial)
        listToStr=''
        for y in initial:
            listToStr +=str(y)+' '
        if x != 49:
            result += listToStr + '\n'
        else:
            result += listToStr
    randomInput= open("input/randomPuzzles.txt", "w")
    randomInput.write(result)

def generateScaledPuzzles():
    initial = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J','K','L']
    result = ''
    for x in range(5):
        random.shuffle(initial)
        listToStr=''
        for y in initial:
            listToStr +=str(y)+' '
        if x != 4:
            result += listToStr + '\n'
        else:
            result += listToStr
    randomInput= open("input/randomScaledPuzzles.txt", "w")
    randomInput.write(result)


def backTrack(goal,closedList):
    result = goal.toString()
    x=goal
    while(x.p_state!=None):
        for y in closedList:
            if (y.c_state == x.p_state):
                result = y.toString() + "\n" + result
                x=y
    return result