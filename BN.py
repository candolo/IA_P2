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
        var_pos = evid.index(-1)
        if len(self.graph[var_pos]) == 1 and evid[self.graph[var_pos][0]] in (0,1):
            return self.prob[var_pos].prob[evid[self.graph[var_pos][0]]]
        else:
            var_unknown_pos = []
            var_true = 0
            var_true_and_false = 0
            
            for k in range(len(self.graph)):
                if evid[k] == []:
                    var_unknown_pos.append(k)
                    
            ev = list(evid)
            
            for i in (0,1):
                ev[var_pos] = i
                for j in (0,1):
                    ev[var_unknown_pos[0]] = j
                    for m in (0,1):
                        ev[var_unknown_pos[1]] = m
                        mult = 1
                        for l in range(len(evid)):
                            mult = mult * self.prob[l].computeProb(tuple(ev))[ev[l]]
                        if i == 1:
                            var_true += mult
                        var_true_and_false += mult
            return var_true/var_true_and_false
        
        
    def computeJointProb(self, evid):
        joint = 1
        for i in range(len(evid)):
                joint = joint * (self.prob[i].computeProb(evid)[evid[i]])
        return joint