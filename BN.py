# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""



class Node():
    def __init__(self, prob, parents = []):
        self.parents = parents
        self.prob = prob
    
    def computeProb(self, evid):
        if len(self.parents) == 0:
            return [1-self.prob[0],self.prob[0]]
        elif len(self.parents) == 1:
            return [1-self.prob[evid[self.parents[0]]], self.prob[evid[self.parents[0]]]]
        elif len(self.parents) == 2:
            return [1-self.prob[evid[self.parents[0]],evid[self.parents[1]]],self.prob[evid[self.parents[0]],evid[self.parents[1]]]]
    
class BN():
    def __init__(self, gra, prob):
        self.graph = gra
        self.prob = prob

    def computePostProb(self, evid):
        pass
               
        return 0
        
        
    def computeJointProb(self, evid):
        joint = 1
        for i in range(len(evid)):
            if evid[i] == 0:
                joint = joint * (self.prob[i].computeProb(evid)[0])
            else:
                joint = joint * (self.prob[i].computeProb(evid)[1])
        return joint