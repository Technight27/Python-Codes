# -*- coding: utf-8 -*-
"""
Created on Tue 20-Aug-2022

@author: Shwashwat Das
"""

#Converting the tuple into a list to be able to change it

x = ("apple","banana","cherry")
print(x)
y = list(x)
print(y)
y[1]="kiwi"
print(y)
x = tuple(y)
print(x)

#zip function:
#It  take items in sequence from a number of collections
#to make a list of tuple, where each tuple 
#contains one item from each collection
A=(1,2,3)
B=("ABC","DEF","GHI")
C=list(zip(A,B))
print(C)
############
C=(1,"ABC"),(2,"DEF"),(3,"GHI")
print(C)
A,B=zip(*C)
print(A)
print(B)
#%%
#Membership test in tuple
my_tuple = {'a','p','p','l','e'}

#In operation
print('a' in my_tuple)
print('g' in my_tuple)

#not in operation 
print('f' not in my_tuple)
#%% using for loop to iteriate through the tuple
for name in ('j','k'):
    print("Hello ", name)
#%%Dispaly even numbers from a tuple
tupple = (2,3,6,11,12,13,17,25,39,43,51,57,103)
print('Tupple = ', tupple)
print('Even numbers from the tuple are as follows: ')
tupple=[x for x in tupple if x%2==0]
print(tupple)
print(type(tupple))