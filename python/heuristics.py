from Node import *
def h1(node,goalState1,goalState2):
    result1=0
    result2=0
    if(node.c_state!=goalState1 and node.c_state!=goalState2):
        for x in range(len(node.c_state)):
            if (node.c_state[x] != 0):
                if node.c_state[x] != goalState1[x]:
                    result1+=1
        for x in range(len(node.c_state)):
            if (node.c_state[x] != 0):
                if node.c_state[x] != goalState2[x]:
                    result2+=1
        node.hn=min(result1,result2)

def h2(node,goalState1,goalState2):
    result1=0
    result2=0
    if (node.c_state != goalState1 and node.c_state != goalState2):
        for x in range(len(node.c_state)):
            if(node.c_state[x]!=0):
                if (abs(goalState1.find(node.c_state[x])-x)==1 or abs(goalState1.find(node.c_state[x])-x)==4):
                    result1+=1
                elif (abs(goalState1.find(node.c_state[x])-x)==2 or abs(goalState1.find(node.c_state[x])-x)==3 or abs(goalState1.find(node.c_state[x])-x)==5 ):
                    result1 += 2
                elif (abs(goalState1.find(node.c_state[x])-x)==6 or abs(goalState1.find(node.c_state[x])-x)==7):
                    result1 += 3

        for x in range(len(node.c_state)):
            if (node.c_state[x] != 0):
                if (abs(goalState2.find(node.c_state[x])-x)==1 or abs(goalState2.find(node.c_state[x])-x)==4):
                    result2+=1
                elif (abs(goalState2.find(node.c_state[x])-x)==2 or abs(goalState2.find(node.c_state[x])-x)==3 or abs(goalState2.find(node.c_state[x])-x)==5 ):
                    result2 += 2
                elif (abs(goalState2.find(node.c_state[x])-x)==6 or abs(goalState2.find(node.c_state[x])-x)==7):
                    result2 += 3
        node.hn=min(result1,result2)

def scaleh2(node,goalState1,goalState2):
    result1=0
    result2=0
    if (node.c_state != goalState1 and node.c_state != goalState2):
        for x in range(len(node.c_state)):
            if(node.c_state[x]!='A'):
                if (abs(goalState1.find(node.c_state[x])-x)==1 or abs(goalState1.find(node.c_state[x])-x)==4):
                    result1+=1
                elif (abs(goalState1.find(node.c_state[x]) - x) == 2 or abs(goalState1.find(node.c_state[x]) - x) == 3 or abs(goalState1.find(node.c_state[x]) - x) == 5 or abs(goalState1.find(node.c_state[x]) - x) == 6 or abs(goalState1.find(node.c_state[x]) - x) == 7 or abs(goalState1.find(node.c_state[x]) - x) == 8 or abs(goalState1.find(node.c_state[x]) - x) == 9 or abs(goalState1.find(node.c_state[x]) - x) == 10 or abs(goalState1.find(node.c_state[x]) - x) == 11):
                    result1 +=2

        for x in range(len(node.c_state)):
            if (node.c_state[x] != 'A'):
                if (abs(goalState2.find(node.c_state[x])-x)==1 or abs(goalState2.find(node.c_state[x])-x)==4):
                    result2 += 1
                elif(abs(goalState2.find(node.c_state[x])-x)==2 or abs(goalState2.find(node.c_state[x])-x)==3 or abs(goalState2.find(node.c_state[x])-x)==5 or abs(goalState2.find(node.c_state[x])-x)==6 or abs(goalState2.find(node.c_state[x])-x)==7 or abs(goalState2.find(node.c_state[x])-x)==8 or abs(goalState2.find(node.c_state[x])-x)==9 or abs(goalState2.find(node.c_state[x])-x)==10 or abs(goalState2.find(node.c_state[x])-x)==11):
                    result2 +=2
        node.hn=min(result1,result2)

temp=Node("12346570",None,0,0,0,"gn",0,0)
h2(temp,"14235670","13572460")


