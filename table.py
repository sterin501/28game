#!/bin/python
import kuthu
import game



class Table(object):
    def __init__(self, p1,p2,p3,p4):
        self.P1=p1
        self.P2=p2
        self.P3=p3
        self.P4=p4
        self.kalli=1
        self.actionAdjust=0 ### To contorl the follow rotation Game
        self.t0base=5
        self.t1base=5
        self.gameCount=0
    def setFirstKalli(self):
            self.gameCount=self.gameCount+1
            self.kalli=(self.gameCount%4)+1
            #print "self kall " + str (self.kalli)
    def getFirstKalli(self):
        if self.kalli==1:
            return ([self.P1,self.P2,self.P3,self.P4])
        elif self.kalli==2:
            return ([self.P2,self.P3,self.P4,self.P1])
        elif self.kalli==3:
           return ([self.P3,self.P4,self.P1,self.P2])
        elif self.kalli==4:
            return ([self.P4,self.P1,self.P2,self.P3])
    def ChangeTheOrderOfPlay(self,newOrder):
       gc=self.gameCount-1
       newOrder=(newOrder-gc)%4
       if newOrder==0:
           self.actionAdjust=newOrder
           return ([self.P1,self.P2,self.P3,self.P4])
       elif newOrder==1:
           self.actionAdjust=newOrder
           return ([self.P2,self.P3,self.P4,self.P1])
       elif newOrder==2:
          self.actionAdjust=newOrder
          return ([self.P3,self.P4,self.P1,self.P2])
       elif newOrder==3:
           self.actionAdjust=newOrder
           return ([self.P4,self.P1,self.P2,self.P3])
