import nashpy as nash
import numpy as np


class Game:
    # create constructor
    def __init__(self) :
        # 0:fire, 1:water , 2:rock , 3:metal ,4:lighning ,5:plant ,
      self.gameMatrix=[
        [" ",    "0",   "1",       "2",           "3",       "4",         "5"    ],
   
        ["0",   (0,0)   ,(4,-4) ,   (0,1) ,     (2,0) ,    (-8, 8) ,  (3,0)  ],
   
        ["1",   (-4,4)  ,(0,0),     (-1,2) ,     (1,0) ,    (-12,12) ,  (4,4)  ],
   
        ["2",   (1,0)   ,(2,-1) ,   (0,0) ,     (1,2) ,   (-20,20) ,  (1,1)  ],
    
        ["3",   (0,2)   ,(0,1) ,   (2,1) ,     (0,0),     (20,-20) ,    (1,-1)  ],
   
        ["4",   (1,2)   ,(3,-3) , (0,1),     (4,-5) ,    (0,0) ,        (0,-1)],
    
        ["5",   (0,3)   ,(4,4) , (1,1) ,    (-1,1) ,   (-1,0) ,        (0,0)],
    ]

    
    
    # calculate dominante strat
    def stratégieDominante(self):
        result=[]
        for i in range(1,len(self.gameMatrix)):
            dominante=True
            for j in range(1,len(self.gameMatrix[0])):
                gain= self.gameMatrix[i][j]
                if gain[0]< gain[1] or gain[0]==gain[1]:
                    dominante=False
            if dominante:
                result.append(i)
    
        return result
    


    # calculate nash equilibrium
    def nashEquilibrium(self):
        result=[]
        l=len(self.gameMatrix)
        c=len(self.gameMatrix[0])
        R1=[]
        R1st=[]
        for j in range(1,c):
            number=self.gameMatrix[1][j]
            pos=1
            max=number[0]
            for i in range(1,l):
                newnumber=self.gameMatrix[i][j]
                if newnumber[0]>max:
                    max=newnumber[0]
                    number=self.gameMatrix[i][j]
                    pos=i
            R1.append(number)
            R1st.append(pos)

        R2=[]
        R2st=[]
        for i in range(1,l):
            number=self.gameMatrix[i][1]
            max=number[1]
            pos=1
            for j in range(1,c):
                newnumber=self.gameMatrix[i][j]
                if newnumber[1]>max:
                    max=newnumber[1]
                    number=self.gameMatrix[i][j]
                    pos=j
            R2.append(number)
            R2st.append(pos)

        for i in range(len(R1)):
            for j in range(len(R2)):
                if R1[i]==R2[j]:
                    result.append(R1st[i])
        return result



    # calculate level of security
    def niveauSecurite(self):
        result=[]
        for i in range(1,len(self.gameMatrix)):
            gain=self.gameMatrix[i][1]
            min=gain[0]
            for j in range(1,len(self.gameMatrix[0])):
                gain=self.gameMatrix[i][j]
                if gain[0]<min:
                    min = gain[0]
            result.append(min)
        max = result[0]
        pos = 0
        for i in range(len(result)):
            if result[i]>max:
                max=result[i]
                pos=i
        return pos+1

    # remove column from game matrix 
    def removeColumn(self,poscol):
        result=self.gameMatrix.copy()
        for i in range(len(self.gameMatrix)):
            result[i].pop(poscol)
        return result



    # get the best choice 
    def bestChoice(self,lt):
        if len(lt)>0:
            gain=self.gameMatrix[lt[0]][1]
            max=gain[0]
            pos=0
            for i in lt:
                for j in range(1,len(self.gameMatrix[0])):
                    gain=self.gameMatrix[i][j]
                    if gain[0]>max:
                        max= gain[0]
                        pos=i
            return pos+1
    

    #make a play

    def makeAPlay(self,playerPlays):

      machinePlays = 1
      strategie = 0
      if len(self.stratégieDominante())>0 :
        machinePlays=self.bestChoice(self.stratégieDominante())
        strategie="Strategie dominante"
      elif len(self.nashEquilibrium())>0:
        machinePlays = self.bestChoice(self.nashEquilibrium())
        strategie="equlibre de nash"
      else:
        machinePlays = self.niveauSecurite()
        strategie="Niveau de securité"
      
    
      
      print('machin choosed : '+str(gameMatrix[machinePlays][0])+"  par : "+strategie)
      print('you choosed : '+str(gameMatrix[0][int(playerPlays)]))
      gain=gameMatrix[machinePlays][int(playerPlays)]
      print('gain : '+str(gain))
      scoreMachine = scoreMachine + gain[0]
      scorePlayer = scorePlayer + gain[1]
      gameMatrix.pop(machinePlays)
      gameMatrix=self.removeColumn(int(playerPlays))
      print("Machin's score : "+str(scoreMachine))
      print("your score : "+str(scorePlayer))
      for kk in gameMatrix:
        print(kk)





# def stratégieDominante(matrice):
#   result=[]
#   for i in range(1,len(matrice)):
#     dominante=True
#     for j in range(1,len(matrice[0])):
#       gain= matrice[i][j]
#       if gain[0]< gain[1] or gain[0]==gain[1]:
#         dominante=False
#     if dominante:
#       result.append(i)
    
#   return result

# def EQNASH(game):
#   equilibria = mygame.support_enumeration()
#   return equilibria


# def nashEquilibrium(mat):
#   result=[]
#   l=len(mat)
#   c=len(mat[0])
#   R1=[]
#   R1st=[]
#   for j in range(1,c):
#       number=mat[1][j]
#       pos=1
#       max=number[0]
#       for i in range(1,l):
#           newnumber=mat[i][j]
#           if newnumber[0]>max:
#               max=newnumber[0]
#               number=mat[i][j]
#               pos=i
#       R1.append(number)
#       R1st.append(pos)

#   R2=[]
#   R2st=[]
#   for i in range(1,l):
#       number=mat[i][1]
#       max=number[1]
#       pos=1
#       for j in range(1,c):
#           newnumber=mat[i][j]
#           if newnumber[1]>max:
#               max=newnumber[1]
#               number=mat[i][j]
#               pos=j
#       R2.append(number)
#       R2st.append(pos)

#   for i in range(len(R1)):
#       for j in range(len(R2)):
#           if R1[i]==R2[j]:
#             result.append(R1st[i])
#   return result



# def niveauSecurite(mat):
#   result=[]
#   for i in range(1,len(mat)):
#     gain=mat[i][1]
#     min=gain[0]
#     for j in range(1,len(mat[0])):
#        gain=mat[i][j]
#        if gain[0]<min:
#          min = gain[0]
#     result.append(min)
#   max = result[0]
#   pos = 0
#   for i in range(len(result)):
#     if result[i]>max:
#       max=result[i]
#       pos=i
#   return pos+1



# A=np.array([
#     [2,4,0,12,8,3],
#     [-2,0,-4,-8,-12,-1],
#     [0,4,-4,20,-20,-2],
#     [0,-4,4,-20,20,-2],
#     [0,20,-20,100,-100,10],
#     [0,-20,20,-100,100,-10]
# ])
# B=-A
# Luckgame=nash.Game(A,B)


# def bestChoice(mat,lt):
#   if len(lt)>0:
#     gain=mat[lt[0]][1]
#     max=gain[0]
#     pos=0
#     for i in lt:
#       for j in range(1,len(mat[0])):
#         gain=mat[i][j]
#         if gain[0]>max:
#           max= gain[0]
#           pos=i
#     return pos+1



# def removeColumn(mat,poscol):
#   result=mat.copy()
#   for i in range(len(mat)):
#     result[i].pop(poscol)
#   return result


# scoreMachine=50
# scorePlayer=50
# while scoreMachine > 0 and scorePlayer > 0 and len(gameMatrix)>1:
#   machinePlays = 1
#   strategie = 0
#   if len(stratégieDominante(gameMatrix))>0 :
#     machinePlays=bestChoice(gameMatrix,stratégieDominante(gameMatrix))
#     strategie="Strategie dominante"
#   elif len(nashEquilibrium(gameMatrix))>0:
#     machinePlays = bestChoice(gameMatrix,nashEquilibrium(gameMatrix))
#     strategie="equlibre de nash"
#   else:
#     machinePlays = niveauSecurite(gameMatrix)
#     strategie="Niveau de securité"
#   print("machine has choosed its strategie, your choises are : ")
#   for choice in range(1,len(gameMatrix[0])):
#     print(str(choice)+" : "+str(gameMatrix[0][choice]))
  
#   playerPlays=input("what's your move ?\n")
#   print('machin choosed : '+str(gameMatrix[machinePlays][0])+"  par : "+strategie)
#   print('you choosed : '+str(gameMatrix[0][int(playerPlays)]))
#   gain=gameMatrix[machinePlays][int(playerPlays)]
#   print('gain : '+str(gain))
#   scoreMachine = scoreMachine + gain[0]
#   scorePlayer = scorePlayer + gain[1]
#   gameMatrix.pop(machinePlays)
#   gameMatrix=removeColumn(gameMatrix,int(playerPlays))
#   print("Machin's score : "+str(scoreMachine))
#   print("your score : "+str(scorePlayer))
#   for kk in gameMatrix:
#     print(kk)



# if scoreMachine <0 :
#   print("yeeeeeeees, you won!")
# elif scorePlayer < 0 :
#   print("Machin won, best of luck next time")
# else: 
#   if scoreMachine > scorePlayer : 
#     print("Machin won, best of luck next time")
#   elif scoreMachine == scorePlayer:
#     print("it's a tie !")
#   else:
#     print("yeeeeeeees, you won!")