#!/usr/bin/env python
# coding: utf-8

# In[107]:


print("Hello, welcome to my portfolio :)")
print ("Here are some practice exercises,just for practice")


# In[34]:


def bla():
    i=0
    for i in range(20):
        i=i+1 
    return i
bla()


# In[35]:


def suma(a,b):
    x=a+b
    return print("La suma de ambos es",x)
    


# In[36]:


suma(28,90)


# In[37]:


def resta(a,b):
    y=a-b
    return print("La resta es",y)


# In[38]:


resta(39,12)


# In[39]:


def mul(a,b):
    z=a*b
    return print("La multiplicacion es",z)


# In[40]:


mul(20,67)


# In[64]:


print("Let's play rock,scissors and paper")
a=str(input("Choose one..."))
if a=="rock":
    b="scissors"
elif a=="scissors":
    b="rock"
elif a=="paper":
    b="scissors"
else:
    print("Please choose rock,scissors or paper")

print("I choose",b,"better luck next time")
   


# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

# In[93]:


def fibo():
    a=int(input("How many numbers? "))
        
    return x3
  


# In[94]:


fibo()


# ## Exercise 1:
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# In[102]:


def year():
    a=input("Please enter your name: ")
    b=int(input("Please enter your age: "))
    x=100-b
    y=2020+x
    return print(a,", you will turn 100 years old in ",y)


# In[103]:


year()


# ## Exercise 2:
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
# 
# Extras:
# 
#     If the number is a multiple of 4, print out a different message.
#     Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
# 

# In[128]:


def nu():
  a=int(input("Please, type a number .. "))
  if a % 2 != 0:
        return print("The number is odd ")
  elif a % 2 == 0:
        return print("The number is even ")
  else:
        return print("Don't enter text, please enter a number")
        


# In[129]:


nu()
        


# In[ ]:





# In[ ]:




