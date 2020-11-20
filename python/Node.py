def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

class Node:
    def __init__(self, c_state,p_state, gn,hn,fn,decision, moveCost,moveTile):
        self.c_state = c_state
        self.p_state = p_state
        self.gn=gn
        self.hn=hn
        self.fn=fn
        self.decision=decision
        self.moveCost=moveCost
        self.moveTile=moveTile
        self.nextSteps=[];

    def toString(self):
        current_state=' '.join([self.c_state[i:i + 1] for i in range(0, len(self.c_state), 1)])
        return (f"{self.moveTile} {self.moveCost} {current_state}")

    def toSearchString(self):
        current_state=' '.join([self.c_state[i:i + 1] for i in range(0, len(self.c_state), 1)])
        return (f"{self.fn} {self.gn} {self.hn} {current_state}")

    def __lt__(self, other):
        if (self.decision=='gn'):
            return self.gn < other.gn
        elif (self.decision=='hn'):
            return self.hn<other.hn
        elif (self.decision=='fn'):
            # if(self.fn==other.fn):
            #     if(self.hn>4):
            #         return self.moveCost>other.moveCost
            #     else:
            #         return self.moveCost<other.moveCost
            # else:
                return self.fn<other.fn
        print('no decision')
        return  self.gn<other.gn

    #up,down,left,right,leftWrap//move 0 to left,  rightWrap,diagonal0 ,diagonal1,diagonal2,diagonal3....
    #0 1 2 3
    #4 5 6 7
    def generateNextSteps(self):
        if (self.c_state[0]=='0'):
            self.nextSteps.append("down")
            self.nextSteps.append("right")
            self.nextSteps.append("rightWrap")
            self.nextSteps.append("diagonal5")
            self.nextSteps.append("diagonal7")
        elif (self.c_state[1]=='0'):
            self.nextSteps.append("down")
            self.nextSteps.append("right")
            self.nextSteps.append("left")
        elif (self.c_state[2]=='0'):
            self.nextSteps.append("down")
            self.nextSteps.append("right")
            self.nextSteps.append("left")
        elif (self.c_state[3]=='0'):
            self.nextSteps.append("down")
            self.nextSteps.append("left")
            self.nextSteps.append("leftWrap")
            self.nextSteps.append("diagonal4")
            self.nextSteps.append("diagonal6")
        if (self.c_state[4]=='0'):
            self.nextSteps.append("up")
            self.nextSteps.append("right")
            self.nextSteps.append("rightWrap")
            self.nextSteps.append("diagonal1")
            self.nextSteps.append("diagonal3")
        elif (self.c_state[5]=='0'):
            self.nextSteps.append("up")
            self.nextSteps.append("right")
            self.nextSteps.append("left")
        elif (self.c_state[6]=='0'):
            self.nextSteps.append("up")
            self.nextSteps.append("right")
            self.nextSteps.append("left")
        elif (self.c_state[7]=='0'):
            self.nextSteps.append("up")
            self.nextSteps.append("left")
            self.nextSteps.append("leftWrap")
            self.nextSteps.append("diagonal0")
            self.nextSteps.append("diagonal2")



    def generateSuccessors(self):
            successors=[]
            emptyTile=self.c_state.find("0")
            for x in self.nextSteps:
                if(x=="up"):
                    successors.append(Node(swap(self.c_state,emptyTile,emptyTile-4),self.c_state,self.gn+1,0,0,self.decision,1,self.c_state[emptyTile-4]))
                elif (x=="down"):
                    successors.append(Node(swap(self.c_state,emptyTile,emptyTile+4),self.c_state,self.gn+1,0,0,self.decision,1,self.c_state[emptyTile+4]))
                elif (x=="left"):
                    successors.append(Node(swap(self.c_state,emptyTile,emptyTile-1),self.c_state,self.gn+1,0,0,self.decision,1,self.c_state[emptyTile-1]))
                elif (x=="right"):
                    successors.append(Node(swap(self.c_state,emptyTile,emptyTile+1),self.c_state,self.gn+1,0,0,self.decision,1,self.c_state[emptyTile+1]))
                elif (x=="leftWrap"):
                    successors.append(Node(swap(self.c_state,emptyTile,emptyTile-3),self.c_state,self.gn+2,0,0,self.decision,2,self.c_state[emptyTile-3]))
                elif (x=="rightWrap"):
                    successors.append(Node(swap(self.c_state,emptyTile,emptyTile+3),self.c_state,self.gn+2,0,0,self.decision,2,self.c_state[emptyTile+3]))
                elif (x=="diagonal0"):
                    successors.append(Node(swap(self.c_state,emptyTile,0),self.c_state,self.gn+3,0,0,self.decision,3,self.c_state[0]))
                elif (x == "diagonal1"):
                    successors.append(Node(swap(self.c_state,emptyTile,1),self.c_state,self.gn+3,0,0,self.decision,3,self.c_state[1]))
                elif (x=="diagonal2"):
                    successors.append(Node(swap(self.c_state,emptyTile,2),self.c_state,self.gn+3,0,0,self.decision,3,self.c_state[2]))
                elif (x=="diagonal3"):
                    successors.append(Node(swap(self.c_state,emptyTile,3),self.c_state,self.gn+3,0,0,self.decision,3,self.c_state[3]))
                elif (x=="diagonal4"):
                    successors.append(Node(swap(self.c_state,emptyTile,4),self.c_state,self.gn+3,0,0,self.decision,3,self.c_state[4]))
                elif (x == "diagonal5"):
                    successors.append(Node(swap(self.c_state,emptyTile,5),self.c_state,self.gn+3,0,0,self.decision,3,self.c_state[5]))
                elif (x=="diagonal6"):
                    successors.append(Node(swap(self.c_state,emptyTile,6),self.c_state,self.gn+3,0,0,self.decision,3,self.c_state[6]))
                elif (x=="diagonal7"):
                    successors.append(Node(swap(self.c_state,emptyTile,7),self.c_state,self.gn+3,0,0,self.decision,3,self.c_state[7]))
            return successors
