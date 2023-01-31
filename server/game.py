import nashpy as nash
import numpy as np


class Game:
    # create constructor
    def __init__(self) :
      self.scoreMachine=40
      self.scorePlayer=40
      self.winner = ""
      self.count=0
      self.machineChoice = None
        # 0:fire, 1:water , 2:rock , 3:metal ,4:lighning ,5:plant ,
      self.gameMatrix=[
        [" ",    "0",   "1",       "2",           "3",       "4",         "5"    ],
   
        ["0",   (0,0)   ,(4,-4) ,   (0,1) ,     (2,0) ,    (-8, 8) ,  (3,0)  ],
   
        ["1",   (-4,4)  ,(0,0),     (-1,2) ,     (1,0) ,    (-12,12) ,  (4,4)  ],
   
        ["2",   (1,0)   ,(2,-1) ,   (0,0) ,     (1,2) ,   (0,0) ,  (1,1)  ],
    
        ["3",   (0,2)   ,(0,1) ,   (2,1) ,     (0,0),     (-2,2) ,    (1,-1)  ],
   
        ["4",   (1,2)   ,(3,-3) , (0,1),     (4,-5) ,    (0,0) ,        (0,-1)],
    
        ["5",   (0,3)   ,(4,4) , (1,1) ,    (-1,1) ,   (-1,0) ,        (0,0)],
    ]

    
    
    # calculate dominante strat
    def dominanteStrat(self):
        temp=[]
        for i in range(1,len(self.gameMatrix)):
            dominante=True
            for j in range(1,len(self.gameMatrix[0])):
                gain= self.gameMatrix[i][j]
                if gain[0]< gain[1] or gain[0]==gain[1]:
                    dominante=False
            if dominante:
                temp.append(i)
    
        return temp
    


    # calculate nash equilibrium
    def Nash(self):
        temp=[]
        lines=len(self.gameMatrix)
        colmuns=len(self.gameMatrix[0])
        player1Best=[]
        Player1BestPos=[]
        for j in range(1,colmuns):
            number=self.gameMatrix[1][j]
            pos=1
            max=number[0]
            for i in range(1,lines):
                newnumber=self.gameMatrix[i][j]
                if newnumber[0]>max:
                    max=newnumber[0]
                    number=self.gameMatrix[i][j]
                    pos=i
            player1Best.append(number)
            Player1BestPos.append(pos)

        Player2Best=[]
        Player2BestPos=[]
        for i in range(1,lines):
            number=self.gameMatrix[i][1]
            max=number[1]
            pos=1
            for j in range(1,colmuns):
                newnumber=self.gameMatrix[i][j]
                if newnumber[1]>max:
                    max=newnumber[1]
                    number=self.gameMatrix[i][j]
                    pos=j
            Player2Best.append(number)
            Player2BestPos.append(pos)

        for i in range(len(player1Best)):
            for j in range(len(Player2Best)):
                if player1Best[i]==Player2Best[j]:
                    temp.append(Player1BestPos[i])
        return temp



    # calculate level of security
    def securityLevel(self):
        temp=[]
        for i in range(1,len(self.gameMatrix)):
            gain=self.gameMatrix[i][1]
            min=gain[0]
            for j in range(1,len(self.gameMatrix[0])):
                gain=self.gameMatrix[i][j]
                if gain[0]<min:
                    min = gain[0]
            temp.append(min)
        max = temp[0]
        pos = 0
        for i in range(len(temp)):
            if temp[i]>max:
                max=temp[i]
                pos=i
        return pos+1

    # remove column from game matrix 
    def removeColumn(self,PosTobeRemoved):
        temp=self.gameMatrix.copy()
        for i in range(len(self.gameMatrix)):
            temp[i].pop(PosTobeRemoved)
        return temp



    # get the best choice 
    def makeAChoice(self,temp):
        if len(temp)>0:
            gain=self.gameMatrix[temp[0]][1]
            max=gain[0]
            pos=0
            for i in temp:
                for j in range(1,len(self.gameMatrix[0])):
                    gain=self.gameMatrix[i][j]
                    if gain[0]>max:
                        max= gain[0]
                        pos=i
            return pos+1
    

    #make a play

    def makeAPlay(self,PlayerChoice):
        
            MachineChoice = 1
           
            if len(self.dominanteStrat())>0 :
                MachineChoice=self.makeAChoice(self.dominanteStrat())
                
            elif len(self.Nash())>0:
                MachineChoice = self.makeAChoice(self.Nash())
                
            else:
                MachineChoice = self.securityLevel()
                
            
            
            
            
            gain=self.gameMatrix[MachineChoice][int(PlayerChoice)]
            self.scoreMachine = self.scoreMachine + gain[0]
            self.scorePlayer = self.scorePlayer + gain[1]
            self.gameMatrix.pop(MachineChoice)
            self.gameMatrix=self.removeColumn(int(PlayerChoice))
            
            self.count +=1
            return MachineChoice





