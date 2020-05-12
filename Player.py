#!/bin/python
import kuthu


class Player(object):
    def __init__(self, name,team,bot):
        self.name = name
        self.hand = []
        self.bot=bot
        self.team=team


    def doTheDeal(self,hand):
         self.hand=hand


    def sayHello(self):
        print "Hi! My name is {} and I am bot =  {}".format(self.name,self.bot)
        return self
    # Display all the cards in the players hand
    def showHand(self):
        print "{}'s hand: {}".format(self.name, self.hand)
        return self

    def showHandinUTF(self):
        dis=""
        for kk in self.hand:
            if kk[0] == ("S"):
                dis=dis+(u"\u2660 "+kk[1])+"   "
            elif kk[0] == ("C"):
                dis=dis+(u"\u2663 "+kk[1])+"   "
            elif kk[0] == ("H"):
                dis=dis+(u"\u2665\uFE0F "+kk[1])+"   "
            elif kk[0] == ("D"):
                dis=dis+(u"\u2666\uFE0F "+kk[1])+"   "
        print dis

    def removeCard(self,chittu):
        self.hand.remove(chittu)



#
# if __name__ == "__main__":
#     ss=kuthu.Card()
#     P1=Player("p1",ss.p1)
#     P2=Player("p2",ss.p2)
#     P3=Player("p3",ss.p3)
#     P4=Player("p4",ss.p4)
#     P1.sayHello()
#     P4.showHand()
#     #P4.removeCard("CT")
#     P4.showHandinUTF()
