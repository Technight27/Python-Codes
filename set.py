# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 00:15:25 2012

@author: Sayan Modal
"""
#~~~~~~~~~~~~~~SET~~~~~~~~~~~~~~
#mutable,...enclosed inside curly brackets
set1={"apple","banana","cherry"}
set2={"a","b","c"}
set3={1,2,3}
set4={1,2,3,4,5}
print(set1)
print(set2)
print(set3)
print(set4)
print(type(set1))
#
print("banana" in set1)
print("grape" in set1)
print("banana" not in set1)

#adding items
set1.add("orange")
print(set1)
#adding multiple items in a set
set1.update(["avacado","lichu","pineapple"])
print(set1)
set2.update(set3)
print(set2)

#remove item
set1.remove("banana")
print(set1)
set1.discard("lichu")
print(set1)
x = set1.pop() #removes the last item in the set 
print(x)
print(set1)

#sets are unordered, so when we use pop we would not know which element popped 

#emptying the set
set1.clear()
print(set1)

#deleting a set
set3={1,2,3}
set4={1,2,3,4,5}
print(set3.issubset(set4))
print(set4.issuperset(set3))

#union, intersection ,difference
#union() method returns a new set with all items from both sets
set5=set3.union(set4)
print(set5)
#union() and update() will exclude any duplicate elements
set3={1,2,3}
set4={1,2,3,4,5}
print(set4.intersection(set3))
#~~~~~~~
set3={1,2,3}
set4={1,2,3,4,5}

print(set4.difference(set3))
