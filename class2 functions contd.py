# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 01:12:06 2012

@author: student
"""

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