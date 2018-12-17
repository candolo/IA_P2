# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""
#test

import numpy as np
from itertools import product

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

        combs = list(product([0,1], repeat=len(evid)))

        valid = True
        for t in combs:
            for i in range(len(t)):
                if evid[i] in (0,1) and evid[i] != t[i]:
                    valid = False
            if valid:
                joint = self.computeJointProb(t)
                if t[var_pos] == 1:
                    var_true += joint
                var_true_and_false += joint
            valid = True

        return var_true/var_true_and_false


    def computeJointProb(self, evid):
        joint = 1
        for i in range(len(evid)):
                joint = joint * (self.prob[i].computeProb(evid)[evid[i]])
        return joint
