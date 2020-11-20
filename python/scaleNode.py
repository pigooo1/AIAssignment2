def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

class scaleNode:
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
            if(self.fn==other.fn):
                if(self.hn>4):
                    return self.moveCost>other.moveCost
                else:
                    return self.moveCost<other.moveCost
            else:
                return self.fn<other.fn
        print('no decision')
        return  self.gn<other.gn

    #up,down,left,right,leftWrap//move 0 to left,  rightWrap,diagonal0 ,diagonal1,diagonal2,diagonal3....
    #A B C D
    #E F G H
    #I J K L
    def generateNextSteps(self):
        if (self.c_state[0]=='A'):
            self.nextSteps.append("down")
            self.nextSteps.append("right")
            self.nextSteps.append("rightWrap")
            self.nextSteps.append("downWrap")
            self.nextSteps.append("diagonalF")
            self.nextSteps.append("diagonalL")
        elif (self.c_state[1]=='A'):
            self.nextSteps.append("down")
            self.nextSteps.append("right")
            self.nextSteps.append("left")
        elif (self.c_state[2]=='A'):
            self.nextSteps.append("down")
            self.nextSteps.append("right")
            self.nextSteps.append("left")
        elif (self.c_state[3]=='A'):
            self.nextSteps.append("down")
            self.nextSteps.append("left")
            self.nextSteps.append("leftWrap")
            self.nextSteps.append("downWrap")
            self.nextSteps.append("diagonalI")
            self.nextSteps.append("diagonalG")
        elif (self.c_state[4]=='A'):
            self.nextSteps.append("up")
            self.nextSteps.append("right")
            self.nextSteps.append("down")
        elif (self.c_state[5]=='A'):
            self.nextSteps.append("up")
            self.nextSteps.append("right")
            self.nextSteps.append("left")
            self.nextSteps.append("down")
        elif (self.c_state[6]=='A'):
            self.nextSteps.append("up")
            self.nextSteps.append("right")
            self.nextSteps.append("left")
            self.nextSteps.append("down")
        elif (self.c_state[7]=='A'):
            self.nextSteps.append("up")
            self.nextSteps.append("left")
            self.nextSteps.append("down")
        elif (self.c_state[8]=='A'):
            self.nextSteps.append("up")
            self.nextSteps.append("right")
            self.nextSteps.append("rightWrap")
            self.nextSteps.append("upWrap")
            self.nextSteps.append("diagonalF")
            self.nextSteps.append("diagonalD")
        elif (self.c_state[9]=='A'):
            self.nextSteps.append("up")
            self.nextSteps.append("right")
            self.nextSteps.append("left")
        elif (self.c_state[10]=='A'):
            self.nextSteps.append("up")
            self.nextSteps.append("right")
            self.nextSteps.append("left")
        elif (self.c_state[11]=='A'):
            self.nextSteps.append("up")
            self.nextSteps.append("left")
            self.nextSteps.append("leftWrap")
            self.nextSteps.append("upWrap")
            self.nextSteps.append("diagonalA")
            self.nextSteps.append("diagonalG")




    def generateSuccessors(self):
            successors=[]
            emptyTile=self.c_state.find("A")
            for x in self.nextSteps:
                if(x=="up"):
                    successors.append(scaleNode(swap(self.c_state,emptyTile,emptyTile-4),self.c_state,self.gn+1,0,0,self.decision,1,self.c_state[emptyTile-4]))
                elif (x=="down"):
                    successors.append(scaleNode(swap(self.c_state,emptyTile,emptyTile+4),self.c_state,self.gn+1,0,0,self.decision,1,self.c_state[emptyTile+4]))
                elif (x=="left"):
                    successors.append(scaleNode(swap(self.c_state,emptyTile,emptyTile-1),self.c_state,self.gn+1,0,0,self.decision,1,self.c_state[emptyTile-1]))
                elif (x=="right"):
                    successors.append(scaleNode(swap(self.c_state,emptyTile,emptyTile+1),self.c_state,self.gn+1,0,0,self.decision,1,self.c_state[emptyTile+1]))
                elif (x=="leftWrap"):
                    successors.append(scaleNode(swap(self.c_state,emptyTile,emptyTile-3),self.c_state,self.gn+2,0,0,self.decision,2,self.c_state[emptyTile-3]))
                elif (x=="rightWrap"):
                    successors.append(scaleNode(swap(self.c_state,emptyTile,emptyTile+3),self.c_state,self.gn+2,0,0,self.decision,2,self.c_state[emptyTile+3]))
                elif (x=="upWrap"):
                    successors.append(scaleNode(swap(self.c_state,emptyTile,emptyTile-8),self.c_state,self.gn+2,0,0,self.decision,2,self.c_state[emptyTile-8]))
                elif (x=="downWrap"):
                    successors.append(scaleNode(swap(self.c_state,emptyTile,emptyTile+8),self.c_state,self.gn+2,0,0,self.decision,2,self.c_state[emptyTile+8]))
                elif (x=="diagonalA"):
                    successors.append(scaleNode(swap(self.c_state,emptyTile,0),self.c_state,self.gn+3,0,0,self.decision,3,self.c_state[0]))
                elif (x == "diagonalG"):
                    successors.append(scaleNode(swap(self.c_state,emptyTile,6),self.c_state,self.gn+3,0,0,self.decision,3,self.c_state[6]))
                elif (x=="diagonalF"):
                    successors.append(scaleNode(swap(self.c_state,emptyTile,5),self.c_state,self.gn+3,0,0,self.decision,3,self.c_state[5]))
                elif (x=="diagonalD"):
                    successors.append(scaleNode(swap(self.c_state,emptyTile,3),self.c_state,self.gn+3,0,0,self.decision,3,self.c_state[3]))
                elif (x=="diagonalI"):
                    successors.append(scaleNode(swap(self.c_state,emptyTile,8),self.c_state,self.gn+3,0,0,self.decision,3,self.c_state[8]))
                elif (x == "diagonalL"):
                    successors.append(scaleNode(swap(self.c_state,emptyTile,11),self.c_state,self.gn+3,0,0,self.decision,3,self.c_state[11]))
            return successors