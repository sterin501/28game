#!/bin/python
import random



class Card(object):
    ## C = Clubs
    ## H = Hearts
    ## S = Spades
    ## D = Diamonds
    def __init__(self):
        self.shape=["C","H","S","D"]
        chittu=["C7","C8","C9","CT","CJ","CQ","CK","CA","H7","H8","H9","HT","HJ","HQ","HK","HA","S7","S8","S9","ST","SJ","SQ","SK","SA","D7","D8","D9","DT","DJ","DQ","DK","DA"]
        order=(random.sample(xrange(0, 32),32))
        #print (order)
        p1=[]
        p2=[]
        p3=[]
        p4=[]
        for kk in range(0,8):
            p1.append(chittu[order[kk]])
        p1.sort()
        self.p1=p1
        for kk in range(8,16):
            p2.append(chittu[order[kk]])
        p2.sort()
        self.p2=p2
        for kk in range(16,24):
            p3.append(chittu[order[kk]])
        self.p3=p3
        for kk in range(24,32):
            p4.append(chittu[order[kk]])
        p4.sort()
        self.p4=p4
