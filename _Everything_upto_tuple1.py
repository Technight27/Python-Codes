# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 01:31:33 2012

@author: Shwashwat Das
"""
# #~~~~~~~~~~~~~~~~~~~~~~~~~Basics
# name1 = "My name is Shwashwat Das"
# name2 = "I study at Calcutta University, Stream: ECE"
# name3 = "I live in Kolkata, near Airport"
# print(name1)
# print(name2)      
# print(name3) 

# #Displaying user's full name
# FName=input("Enter your first name: ")
# SName=input("Enter your sirname: ")
# fullname= FName+ " " + SName
# print(fullname)

# #fahrenheit to celsius conversion
# temp=float(input("Enter temperature in Fahrenheit: "))
# celsius=5*(temp-32)/9
# print("The temp. in celsius is ",celsius)

# #functions
# def name():
#     print("My name is Shwashwat Das")
# name()

# #function to print my fullname
# def fullname():
#     Fname=input("Enter your first name: ")
#     Sname=input("Enter your sirname: ")
#     fullname= Fname+ " " + Sname
#     print(fullname)
# fullname()

# #function for fahrenheit to celsius
# def fahrenheit_to_celsius():
#     temp=float(input("Enter temperature in fahrenheit: "))
#     celsius=5*(temp-32)/9
#     print("The temp. in celsius is ",celsius)
# fahrenheit_to_celsius()
    
# #write a program using if, elif, else
# def if_statement():
#     x=9
#     y=0
#     z=0
#     if x>0:
#         print("x is positive")
        
#     if y>0:
#         print("y is positive")
#     else:
#         print("y is not positive")
        
#     if z>0:
#         print("z is positive")
#     elif z<0:
#         print("z is negative")
#     else:
#         print("z must be zero")
# if_statement()

## def area(type_, x):
#     if type_ =="circle":
#         area=3.1416*(x**2)
#         print(area)
#     elif type_=="square":
#         area=x**2
#     else:
#         print("I don't know")
# area("circle",2)

# #def counting():
#     count=2
#     while count<100:
#         print(count, end=" ")
#         count+=2
#     print()
#     print("Let's go")
# counting()

## def counting2():
#     for count in range(2,100,2):
#         print(count, end=" ")
#     print()
#     print("Let's go")
# counting2()

#reverse countdown
# def count_down():
#     count=100
#     while count>0:
#         print(count,end=" ")
#         count-=1
#     print()
#     print("Rocket Launched!")
# count_down()

# #reverse countdown with limit
# def count_down2():
#     for count in range(100,0,-1):
#         print(count,end=" ")
#     print()
#     print("Rocket again launched!!")
# count_down2()


##//~~~~~~~~~~~~~~~~~~~~DATE 30-Aug-2022
# #write a function to count nos. from a particular no. to another limit
# for count in range(2,100,2):
#     # range(x,y,z) : x=start, y=less than not equal to, z=step
#     print(count, end=" ")
# print()
# print("Let's go")

# #Rocket Launcher
# for i in range(100,1,-1):
#     print(i,end=" ")
# print()
# print("Rocket Launched!")

# #write a program using FOR loop to print the factorial of anumber
# num = int(input("Enter the number: "))
# count = 1
# result = 1
# for count in range(1,num,1):
#     result*=count
#     count+=1
# print("Factorial of number ", num, " is ",result)

# #Fibonacci series
# FN = int(input("Please enter the first number: "))
# SN = int(input("Please enter the second number: "))
# limit = int(input("Number of Fibbanacci number to be printed: ")) 
# print(FN, " ", SN, end=" ")
# for i in range (limit+1):
#     sum= FN+SN
#     FN=SN
#     SN=sum
#     print(sum, end=" ")
# print()

# #multiplication table from 1 to 5
# print("Multiplication table from 1 to 5")
# for i in range(1,11,1):
#     for j in range(1,6,1):
#         print(format(i*j,"4d"),end=" ")
#     print()


# # star pattern display
# for i in range (1,6,1):
#     for j in range(1,i+1,1):
#         print(" * ", end= "")
#     print()
# print ("End of Program")


# # star pattern display
# #num=7
# for i in range(7,1,-1):
#     for j in range(1,i-1,1):
#         print(" * ", end="")
#     print()
# print("end of Program")

# #display 1 to 10
# for i in range(1,100,1):
#     if(i==11):
#         break   #immeditately terminated loop
#     else:
#         print(i, end=" ")
# print()
    

# #display 1 to 10
# for i in range(1,11,1):
#     if(i==8):
#         continue   #when encourted in loop, the condition are skipped but continue
#     print(i, end=" ")
# print()

#a number is prime or not
# num= int(input("Enter a number: "))
# for i in range(2, num):
#     if num%i==0:
#         flag=0
#         break
#     else:
#         flag=1
# if flag==1:
#     print(num, "is prime")
# else:
#     print(num, "is not prime ")

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #~~~~~~~~~~~~STRINGS~~~~~~~~~~~~~

# #slicing of strings
# a="I, love my Country!"
# print(a[::])
# print(a[::-1])
# print(a[6])
# print(a[2:10])
# print(a[-7:-2])
# print(len(a))
# print(a[0:len(a):2])

# #%%searching substring in a string
# print(a.endswith("Country"))
# print(a.startswith("Country"))
# print(a.find("Count"))
# print(a.find("Team"))
# print(a.strip())
# print(a.split(","))
# print(a.split(" "))
# print(a.split("."))
# #%%

# #joining strings
# c="Shwashwat"
# b="Sibu"
# print(c+" "+b)


# #format string
# age=21
# t="I am Shwashwat,my age is {}"
# print(t.format(age))

# #to print multiple times
# print(a*3)

# #string comparison
# s1="abc"
# s2="abc"
# s3="def"
# print(s1==s2)
# print(s1>s2)
# print(s1<s2)

# #%% WAP   TO TRAVERSE ALL THE ELEMENTS OF STRING USING FOR LOOP
# for ch in a:
#     print(ch,end="")
# print(" " )

# #%% traverse every second character 
# for ch in range(0,len(a),2):
#      print(a[ch],end="")
# print("")


# #%%wap to print all letters from word1 that appear in word2

# s1="I love python"
# s2="I love matlab"
# print("word1=",s1)
# print("word2=",s2)
# print("letters from word1 that also appear in word2 are")
# for letter in s1:
#     if letter in s2:
#         print(letter,end="")
# print("")        
# #%%


# #%%WAP to take word from user and returns the vowels in that word
# def countvowels(word):
#     print("word= ",word)
#     word=word.lower()
#     return{v:word.count(v) for v in "aeiou:"}
# print(countvowels("i love matlab"))
# #%%
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~LIST~~~~~~~~~~~~~~
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
# #%%

# b=[2,3,4,5,6]
# print(b.clear())
# c=[1,2,3]
# print(3*c)
# c.reverse()
# print(c)
# c.sort()
# print(c)

# #~~~~~~~~~~~~~~~~~~~~~~
# #19-Aug-2022
# #~~~~~~~~~~~~~~~~~~~~~~

# #~~~~~~~~~~~~~~SET~~~~~~~~~~~~~~
# #mutable,...enclosed inside curly brackets
# set1={"apple","banana","cherry"}
# set2={"a","b","c"}
# set3={1,2,3}
# set4={1,2,3,4,5}
# print(set1)
# print(set2)
# print(set3)
# print(set4)
# print(type(set1))
# #
# print("banana" in set1)
# print("grape" in set1)
# print("banana" not in set1)

# #adding items
# set1.add("orange")
# print(set1)
# #adding multiple items in a set
# set1.update(["avacado","lichu","pineapple"])
# print(set1)
# set2.update(set3)
# print(set2)

# #remove item
# set1.remove("banana")
# print(set1)
# set1.discard("lichu")
# print(set1)
# x = set1.pop() #removes the last item in the set 
# print(x)
# print(set1)

# #sets are unordered, so when we use pop we would not know which element popped 

# #emptying the set
# set1.clear()
# print(set1)

# #deleting a set
# set3={1,2,3}
# set4={1,2,3,4,5}
# print(set3.issubset(set4))
# print(set4.issuperset(set3))

# #union, intersection ,difference
# #union() method returns a new set with all items from both sets
# set5=set3.union(set4)
# print(set5)
# #union() and update() will exclude any duplicate elements
# set3={1,2,3}
# set4={1,2,3,4,5}
# print(set4.intersection(set3))
# #~~~~~~~
# set3={1,2,3}
# set4={1,2,3,4,5}

# print(set4.difference(set3))


# #~~~~~~~~~~~~~Tuple~~~~~~~~~~~
# T1=()
# print(T1)

# T2=(10,20,30,40)
# print(T2)

# T3=('a','b','c','d')
# print(T3)

# T4='a','b','c','d' #it is assumed tuple
# print(T4)

# tup1=("apple","banana","cherry","stawberry")
# print(tup1)

# T5=(5,)
# print(T5)

# I=(5)
# print(I)

# T6=("APPLE")
# print(T6)

# #printing the type
# print(type(T1))
# print(type(T5))
# print(type(T4))
# print(type(I))

# ##slicing
# print(tup1[1])
# print(tup1[-1])
# print(tup1[1:])
# print(tup1[:1])
# print(tup1[0:3])

# #inbuilt functions
# print(len(T1))
# print(max(T1))
# print(min(T1))
# print(sum[T1])
# print(len(T6))
# print(min(T6))
# print(max(T6))
# #print(sum(T6)) ##Error

# #operations
# tup1=(12,2.4)
# tup2=('abc','xy12')
# tup3=tup1+tup2
# print(tup3)

# #tuples are unchangeable so we can just delete them
# tup4=("apple","banana","cherry")
# print(tup4)
# del tup4

#~~~~~~~~~~~~~~~~~~~~~~
#20-Aug-2022
#~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~TUPLE Contd......
#Conterting the tuple into a list to be able to change it
x = ("apple","banana","cherry")
 