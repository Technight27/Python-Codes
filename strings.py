# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 01:12:42 2012

@author: student
"""
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