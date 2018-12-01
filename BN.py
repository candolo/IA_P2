# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

import numpy as np

class Node():
    def __init__(self, prob, parents = []):
        self.parents = parents
        self.prob = prob
    
    def computeProb(self, evid):
        parents_ev = []
        
        for i in self.parents:
            parents_ev.append(evid[i])
        
        return [1-self.prob[tuple(parents_ev)],self.prob[tuple(parents_ev)]]
    
class BN():
    def __init__(self, gra, prob):
        self.graph = gra
        self.prob = prob

    def computePostProb(self, evid):
        var_pos = evid.index(-1)
        var_true = 0
        var_true_and_false = 0
        
        for e1 in (0,1):
            if evid[0] in (0,1) and e1 != evid[0]:
                continue            
            for e2 in (0,1):
                if evid[1] in (0,1) and e2 != evid[1]:
                    continue                
                for e3 in (0,1):
                    if evid[2] in (0,1) and e3 != evid[2]:
                        continue                    
                    for e4 in (0,1):
                        if evid[3] in (0,1) and e4 != evid[3]:
                            continue
                        for e5 in (0,1):
                            if evid[4] in (0,1) and e5 != evid[4]:
                                continue
                            
                            ev = (e1,e2,e3,e4,e5)
                            joint = self.computeJointProb(ev)
                            if ev[var_pos] == 1:
                                var_true += joint
                            var_true_and_false += joint
                            
        return var_true/var_true_and_false
        
        
    def computeJointProb(self, evid):
        joint = 1
        for i in range(len(evid)):
                joint = joint * (self.prob[i].computeProb(evid)[evid[i]])
        return joint