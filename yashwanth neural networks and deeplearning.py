#!/usr/bin/env python
# coding: utf-8

# In[11]:


#1)Write a program that takes two strings from the user and need to join them
def word(word1,word2):
  print(word1+" "+word2)

first_name=input("enter first name : ")
last_name=input("enter second name : ")
word(first_name,last_name)


# In[12]:


#1.2)Write function named “string_alternative” that returns every other char in the full_name string.
def string_alternative(my_word):
  result=my_word[::2]
  print(result)
def main():
  my_word=input("enter the string : ")
  string_alternative(my_word)
if __name__=="__main__":
  main()


# In[14]:


#2)Write a python program to find the wordcount in a file (input.txt) for each line and then print the output. 
file = open("yashipc2.txt", "r")
k= dict()
for sentence in file:
    sentence = sentence.strip()
    sentence = sentence.lower()
    print(sentence)
    words = sentence.split(" ")
                
    for word in words:
        if word in k:
            k[word] = k[word] + 1
        else:
            k[word] = 1
for key in list(k.keys()):
    print(key, ":", k[key])
file.close()


# In[15]:


##3)Write a program, which reads heights (inches.) and converts to centimeter.
lst=[]
n=int(input("enter number of elements : "))
for i in range(0,n):
  a=int(input())
  lst.append(a)
print(lst)
l2=[]
for j in lst:
  j=j/2.54
  k=round(j,2)
  l2.append(k)
print(l2)


# In[ ]:




