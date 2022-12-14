#!/usr/bin/env python
# coding: utf-8

# In[5]:


x = 5
print(x)


# In[6]:


y = 8


# In[7]:


Y


# In[8]:


y


# In[9]:


x, y = (1, 2)
print(x, y)


# In[10]:


x1 = 5


# In[12]:


type(x1)


# In[13]:


x2 = 4.25


# In[14]:


type(x2)


# In[1]:


int(3.14)


# In[3]:


x3 = True


# In[4]:


type(x3)


# In[5]:


'George'


# In[6]:


x4 = 'George'


# In[7]:


x4


# In[12]:


y = 10


# In[13]:


str(y)


# In[15]:


print (str(y) + " Dollars")


# In[16]:


"I'm fine."


# In[3]:


def add_ten(m):
    if m >= 100:
        m += 10
        return m
    else:
        print("Save more!")


# In[4]:


add_ten(100)


# In[5]:


add_ten(50)


# In[4]:


pow(10, 2)


# In[5]:


pow(2, 3)


# In[6]:


Participants = ["John", "Mary", "Jane", "Bob"]
Participants


# In[7]:


print(Participants[1])


# In[8]:


Participants[-2]


# In[9]:


Participants[3] = "Pete"


# In[10]:


Participants


# In[11]:


del Participants[0]


# In[12]:


Participants


# In[13]:


Participants.append("Mark") # calls in or invokes a method


# In[14]:


Participants


# In[34]:


Participants.extend(["Kate", "Cristina", "Derek"]) # using extend allows to add multiple elements to the list.
Participants


# In[ ]:





# In[25]:


Participants


# In[27]:


del Participants[-1]


# In[30]:


Participants.append("Derek")


# In[31]:


Participants


# In[32]:


del Participants[3]


# In[35]:


Participants


# In[36]:


del Participants[-1]


# In[40]:


Participants


# In[41]:


Participants[1:3] # list slicing


# In[42]:


Participants[:2] # first two items from the list


# In[43]:


Participants[4:] # from 4th position to the end of the list


# In[44]:


Participants[-2:] # the last two items


# In[45]:


Participants.index("Cristina")


# In[46]:


Newcommers = ["Joshua", "Britney"]
Newcommers


# In[48]:


Bigger_List = [Participants, Newcommers]
Bigger_List


# In[57]:


def sortByName(list):
    list.sort()
    return list

sortByName(Participants)
sortByName(Newcommers)

Bigger_List


# In[62]:


Numbers =[4, 6, 2, 7, 9, 3, 1]
Numbers.sort()
print(Numbers)


# In[65]:


# Tuples - Ordered and Immutable Lists
x = (35, 40, 45, 50)
x


# In[66]:


x[2]


# In[67]:


y = (10, 20, 25)
List_1 = [y, x]
List_1


# In[69]:


(age, year_of_school) = "35,17".split(",") # comma-separated value splitting
print(age)
print(year_of_school)


# In[70]:


# returning tuples as return values
def square_info(x):
    A = x ** 2
    B = 4 * x
    print("Area and Perimeter:")
    return A,B

square_info(3)


# In[75]:


# Dictionaries - Collections of data in key:value pairs

# A dictionary is a collection which is ordered*, 
# changeable and do not allow duplicates.

dict = {
    'animal1': 'shark',
    'animal2': 'koala',
    'animal3': 'fish'
}


# In[76]:


dict['animal2']


# In[77]:


dict['animal3']


# In[78]:


dict['animal4'] = 'parrot'
dict


# In[79]:


dict['animal1'] = 'squirrel'


# In[80]:


dict


# In[81]:


dept_workers = {
    'dept1': 'Peter',
    'dept2': [
        'Jane',
        'Mark',
        'Derek'
    ]
}
dept_workers


# In[83]:


Team = {}
Team['Front Player'] = 'Dirk'
Team['Center Player'] = 'Joan'
Team['Back Player'] = 'Louis'

Team


# In[84]:


print(Team['Center Player'])


# In[87]:


print(Team.get('Coach')) # Won't display error if the value requested doesn't actually exist in a given dictionary.


# In[90]:


# Iterations

even = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in even:
    print (n, end = " ")


# In[94]:


x = 0

while x < 20:
    x += 2
    print(x, end = " ")


# In[96]:


# Creation of Lists with the range() Function

# range(start, stop, step)

# start = the first number in the list
# stop = the last value +1
# step = the distance between each two consecutive values 

# stop is required, start & step are optional

# If the values are not provided,
# start = 0 and step = 1

range(10) # it will stop before getting to the stop value


# In[97]:


list(range(10)) # list created from a range


# In[100]:


list(range(1, 7))


# In[101]:


list(range(1, 20, 2))


# In[102]:


list(range(0, 20, 2))


# In[103]:


# Quick Summary

# The range() function can be used to create lists with
# a given set of start, stop and step values.


# In[104]:


for n in range(10):
    print (2 ** n, end = " ")


# In[109]:


# Combination of Iteration and Conditional

for x in range(20):
    if x % 2 == 0:
        print (x, end = " ")
    else: print ('Odd', end = " ")


# In[111]:


def count(numbers): # counting how many numbers are below 20
    total = 0 # rolling sum
    for x in numbers:
        if x < 20:
            total += 1
    return total 

list_1 = [2, 3, 4, 78, 54, 23, 8, 17, 11, 24]

count(list_1)


# In[116]:


# Iteration over Dictionaries

prices = {
    'pencil': 6,
    'eraser': 4,
    'pen': 2
}

quantity = {
    'pencil': 6,
    'eraser': 4,
    'pen': 2
}

money_spent = 0

for i in prices:
    money_spent += (prices[i] * quantity[i])

print (money_spent) 


# In[ ]:




