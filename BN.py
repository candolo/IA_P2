# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

import copy


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
        if len(self.graph[evid.index(-1)]) == 1 and evid[self.graph[evid.index(-1)][0]] in (0,1):
            return self.prob[evid.index(-1)].prob[evid[self.graph[evid.index(-1)][0]]]
        else:
            var_pos = evid.index(-1)
            var_pos_empty = []
            var_equals_1 = 0
            var_equals_1_and_0 = 0
            var_pos = evid.index(-1)
            
            for k in range(len(evid)):
                if evid[k] == []:
                    var_pos_empty.append(k)
                    
            ev = list(evid)
            
            for i in range(2):
                ev[var_pos] = i
                for j in range(2):
                    ev[var_pos_empty[0]] = j
                    for m in range(2):
                        ev[var_pos_empty[1]] = m
                        mult = 1
                        for l in range(len(evid)):
                            mult = mult * self.prob[l].computeProb(tuple(ev))[ev[l]]
                        if i == 1:
                            var_equals_1 += mult
                        var_equals_1_and_0 += mult
            return var_equals_1/var_equals_1_and_0
        
        
    def computeJointProb(self, evid):
        joint = 1
        for i in range(len(evid)):
                joint = joint * (self.prob[i].computeProb(evid)[evid[i]])
        return joint