# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 01:01:47 2012

@author: student
"""

D1 ={"Name":"DEF","Age":6,"Class":"two"}
print(D1)

####
D2={}
D2['Name']='DEF'
D2['Age']=6
D2['Class']='two'
print(D2)

###
D3=dict(Name="DEF", Age=6, Class="two")
print(D3)

###
D4=dict([('Name', "DEF"),('Age', 6),('Class',"two")])
print(D4)

#Show the elements
print("'dictionary['Name'] is : ", D1["Name"])
print("'dictionary['Age'] is : ", D1["Age"])
print("'dictionary['Class''] is : ", D1["Class"])

#%%updating elements
D4["Age"]=8
D4["Class"]='three'
print(D4)
print(type(D4))
#%%Deleting dictionary elements
del D1['Name']
print(D1)
D1.clear()
print(D1)
del D1
#print(D1)
# #%%comparing dictionaries
# if D2==D3:
#     print("Equal!!!")
#%%a database of phone numbers could be stored in a dictionary
phonebook={}
phonebook["John"]=938477566
phonebook["Jack"]=938477564
phonebook["Jill"]=947789566
print(phonebook)
#%%Iterating over a dictionaries
for name, number in phonebook.items() :
    print("Phone number of %s is %d" %(name, number))
#%%Removing a value 
del phonebook["John"]
print(phonebook)
#%%testing code......
if "Jack" in phonebook:
    print("Jack is listed in phonebook.")
if "Jacob" not in phonebook:
    print("Jacob is not in phonebook")
#%%nested dictionary
#dictionary within a dictionary  is called 
Players={"Kohli":{"ODI" : 7212,"Test" : 3245},"Tendulkar":{"ODI" : 18426 , "Test" : 15921}}
print(Players)
for Players_name, Players_details in Players.items():
    print("" , Players_name)
    print("" , Players_details)
    print("Run scored in ODI: \t", Players_details["ODI"])
    print("Run scored in Test: \t", Players_details["Test"])
#%%
'''given a number n, you have to write a program that generates a dictionary containing (i , i*i)
   where  i is from 1 to n
'''
n = int(input())
d = dict()
for i in range(1,n+1):
    d[i] = i*i
print(d)
#%% same as above but with exponentiation operator and using function
def printDict():
    n = int(input())
    d = dict()
    for i in range(1,n+1):
        d[i] = i**2
print(d)
printDict()
