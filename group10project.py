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
constraints.append(c[0,0]==537)
constraints.append(c[0,1]+l[0,0]-l[0,1]==112)
constraints.append(c[0,2]+l[0,1]-l[0,2]==112)
constraints.append(c[0,3]+l[0,2]-l[0,3]==112)
constraints.append(c[0,4]+l[0,3]-l[0,4]==112)
constraints.append(c[0,5]+l[0,4]-l[0,5]==112)
constraints.append(c[0,6]+l[0,5]-l[0,6]==112)
constraints.append(c[0,7]+l[0,6]-l[0,7]==112)
constraints.append(c[0,8]+l[0,7]==112)  

constraints.append(c[1,0]==537)
constraints.append(c[1,1]+l[1,0]-l[1,1]==112)
constraints.append(c[1,2]+l[1,1]-l[1,2]==112)
constraints.append(c[1,3]+l[1,2]-l[1,3]==112)
constraints.append(c[1,4]+l[1,3]-l[1,4]==112)
constraints.append(c[1,5]+l[1,4]-l[1,5]==112)
constraints.append(c[1,6]+l[1,5]-l[1,6]==112)
constraints.append(c[1,7]+l[1,6]-l[1,7]==112)
constraints.append(c[1,8]+l[1,7]==112) 

constraints.append(c[2,0]==537)
constraints.append(c[2,1]+l[2,0]-l[2,1]==112)
constraints.append(c[2,2]+l[2,1]-l[2,2]==112)
constraints.append(c[2,3]+l[2,2]-l[2,3]==112)
constraints.append(c[2,4]+l[2,3]-l[2,4]==112)
constraints.append(c[2,5]+l[2,4]-l[2,5]==112)
constraints.append(c[2,6]+l[2,5]-l[2,6]==112)
constraints.append(c[2,7]+l[2,6]-l[2,7]==112)
constraints.append(c[2,8]+l[2,7]==112) 


constraints.append(c[0,1]+l[0,0]<=537)
constraints.append(c[0,2]+l[0,1]<=537)
constraints.append(c[0,3]+l[0,2]<=537)
constraints.append(c[0,4]+l[0,3]<=537)
constraints.append(c[0,5]+l[0,4]<=537)
constraints.append(c[0,6]+l[0,5]<=537)
constraints.append(c[0,7]+l[0,6]<=537)
constraints.append(c[0,8]+l[0,7]<=537)

constraints.append(c[1,1]+l[1,0]<=537)
constraints.append(c[1,2]+l[1,1]<=537)
constraints.append(c[1,3]+l[1,2]<=537)
constraints.append(c[1,4]+l[1,3]<=537)
constraints.append(c[1,5]+l[1,4]<=537)
constraints.append(c[1,6]+l[1,5]<=537)
constraints.append(c[1,7]+l[1,6]<=537)
constraints.append(c[1,8]+l[1,7]<=537)

constraints.append(c[2,1]+l[2,0]<=537)
constraints.append(c[2,2]+l[2,1]<=537)
constraints.append(c[2,3]+l[2,2]<=537)
constraints.append(c[2,4]+l[2,3]<=537)
constraints.append(c[2,5]+l[2,4]<=537)
constraints.append(c[2,6]+l[2,5]<=537)
constraints.append(c[2,7]+l[2,6]<=537)
constraints.append(c[2,8]+l[2,7]<=537)




problem = cp.Problem(cp.Minimize(obj_func), constraints)

problem.solve(verbose = True)
problem.solve(solver=cp.GUROBI,verbose = True)

print("obj_func =")
print(obj_func.value)
print("c =")
print(c.value)
print("l =")
print(l.value)