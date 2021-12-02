#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 15:09:18 2021

@author: mimicai
"""

import cvxpy as cp


c = cp.Variable((3,9), nonneg  = True) # vector variable
l = cp.Variable((3,8), nonneg  = True) # vector variable


obj_func= c[0,0]+c[0,1]+c[0,2]+c[0,3]+c[0,4]+c[0,5]+c[0,6]+c[0,7]+c[0,8]\
            +c[1,0]+c[1,1]+c[1,2]+c[1,3]+c[1,4]+c[1,5]+c[1,6]+c[1,7]+c[1,8]\
            +c[2,0]+c[2,1]+c[2,2]+c[2,3]+c[2,4]+c[2,5]+c[2,6]+c[2,7]+c[2,8]

constraints = []
for n in range (3):
    constraints.append(c[n,0]==537)
    for i in range(7):
        constraints.append(c[n,i+1]+l[n,i]-l[n,i+1]==112)
    constraints.append(c[n,8]+l[n,7]==112)  


for n in range (3):
    constraints.append(c[n,0]==537)
    for i in range(7):
        constraints.append(c[n,i+1]+l[n,i]<=537)


problem = cp.Problem(cp.Minimize(obj_func), constraints)

problem.solve(verbose = True)
problem.solve(solver=cp.GUROBI,verbose = True)

print("obj_func =")
print(obj_func.value)
print("c =")
print(c.value)
print("l =")
print(l.value)
