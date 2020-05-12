#!/bin/python
import kuthu
import Player



class Table(object):
    def __init__(self, p1,p2,p3,p4):
        self.P1=p1
        self.P2=p2
        self.P3=p3
        self.P4=p4
        self.t0base=5
        self.t1base=5
        self.gameCount=1
        self.opener=0
        self.orderofPlay=[self.P1,self.P2,self.P3,self.P4]
    def setNextGame(self):
            self.gameCount=self.gameCount+1
            self.opener=(self.gameCount-1)%4
            self.orderofPlay=[self.P1,self.P2,self.P3,self.P4]
            #self.kalli=(self.gameCount%4)+1
            #print "self kall " + str (self.kalli)
    def getOrderOfPlayers(self):
        print ("opener     --->" + str (self.opener))
        temp=[]
        if self.opener==0:
             print('')
        elif self.opener==1:
            temp.append(self.orderofPlay[1])
            temp.append(self.orderofPlay[2])
            temp.append(self.orderofPlay[3])
            temp.append(self.orderofPlay[0])
            self.orderofPlay=temp

        elif self.opener==2:
            temp.append(self.orderofPlay[2])
            temp.append(self.orderofPlay[3])
            temp.append(self.orderofPlay[0])
            temp.append(self.orderofPlay[1])
            self.orderofPlay=temp

        elif self.opener==3:
            temp.append(self.orderofPlay[3])
            temp.append(self.orderofPlay[0])
            temp.append(self.orderofPlay[1])
            temp.append(self.orderofPlay[2])
            self.orderofPlay=temp


        print (self.orderofPlay[0].name + self.orderofPlay[1].name+self.orderofPlay[2].name+self.orderofPlay[3].name)





    #
    # def ChangeTheOrderOfPlay(self,newOrder):
    #    gc=self.gameCount-1
    #    newOrder=(newOrder-gc)%4
    #    if newOrder==0:
    #        self.actionAdjust=newOrder
    #        return ([self.P1,self.P2,self.P3,self.P4])
    #    elif newOrder==1:
    #        self.actionAdjust=newOrder
    #        return ([self.P2,self.P3,self.P4,self.P1])
    #    elif newOrder==2:
    #       self.actionAdjust=newOrder
    #       return ([self.P3,self.P4,self.P1,self.P2])
    #    elif newOrder==3:
    #        self.actionAdjust=newOrder
    #        return ([self.P4,self.P1,self.P2,self.P3])
