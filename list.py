# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 00:03:23 2012

@author: Sayan Mondal
"""

# l=["apple","banana","melon","cherry","guava","chiku","lemon","pineapple"]
# print(l[:-2])
# print(l[:4])
# print(l[-2:])
# print(l[-3:-2])

# print(sum(li))
# l[1]="strawberry"
# print(l)
# l.append("blueberry")
# li=[1,2,6,4,5]
# print(len(li))
# print(min(li))
# print(max(i))
# l.insert(1,"rashberry")
# print(l)
# l.remove("apple")
# print(l)
# #%%delete from list
# a=[1,2,3,4,5,6,7,8]
# del a[0]
# print(a)
# del a[-1]
# print(a)
# del a[1:3]
# print(a)
# del a[:]
# print(a)
# # #%%

# b=[2,3,4,5,6]
# print(b.clear())
# c=[1,2,3]
# print(3*c)
# c.reverse()
# print(c)
# c.sort()
# print(c)




#%%Even nos list
list1=list(range(2,101,2))
print(list1)
#%%return prime numbers frrom list
l=[1,2,3,4,5,67,78,34,45,23,44,45,87]
li=[]
print("prime nos from the list are as follows:\n")
for a in l:
    p=True
    for i in range(2,a):
        if a%i==0:
            p=False
            break;
    if p:
        li.append(a)
print(li)  
#%%Find average nos

                         































