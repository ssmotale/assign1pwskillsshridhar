

"""
Q1. What are the characteristics of the tuples? Is tuple immutable?
ans: tuple is immmutable
"""
"""
Q2. What are the two tuple methods in python? Give an example of each method. Give a reason why
tuples have only two in-built methods as compared to Lists.

ans: count and index are the two methodes used in tuples, 

Reason:As tuple is immutable hence we cant change elements inside tuple once assigned.therefore only 2 methodes 
compared to list which is mutable

"""
t1=(1,2,2,34,5,55,5)
t1.count(2)


# In[10]:


t1=(1,2,2,34,5,55,5)
t1.count(2)
#output=2


# In[16]:


t1=(1,2,2,34,5,55,5)
x = t1.index(2)
x
#out=1


# In[34]:


"""
Q3. Which collection datatypes in python do not allow duplicate items? Write a code using a set to remove
duplicates from the given list.
Ans: set datatype  allow only unique values 
"""
List = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]
a=set(List)
a
id(a)
#output:{1, 2, 3, 4}


# In[33]:


"""
Q4. Explain the difference between the union() and update() methods for a set. Give an example of
each method.

"""
b={5,6,7}
c=a.union(b)
#id(c)
#out:140446792412608
d=a.update(b)
id(d)
#out:94056578422720


#output:{1, 2, 3, 4, 5, 6, 7}
#update gives updated set at same memory location
#union create new memory  location althrough both gives same output


# In[35]:


"""
Q5. What is a dictionary? Give an example. Also, state whether a dictionary is ordered or unordered.

Ans: It is collection of key and value pairs
EX.
dict1={"key1":"value1","key2":"vaalue2"...."keyn":"valuen"}

Dictionaries are ordered
"""


# In[44]:


"""
Q6. Can we create a nested dictionary? If so, please give an example by creating a simple one-level
nested dictionary.
 yes it is possible to create nested dictionary
"""
d2={"ram":{"sham":"sam","aam":"lam"},"d":"f"}
d2
#output:{'ram': {'sham': 'sam', 'aam': 'lam'}, 'd': 'f'}


# In[62]:


"""
Q7. Using setdefault() method, create key named topics in the given dictionary and also add the value of
the key as this list ['Python', 'Machine Learning’, 'Deep Learning']

"""
list3={"topic1":'Python',"topic2":"Machine Learning","topic3":"Deep Learning"}
dt1=list3.setdefault("topic1")
dt2=list3.setdefault("topic2")
dt3=list3.setdefault("topic3")
list[dt1,dt2,dt3]
#output:list['Python', 'Machine Learning', 'Deep Learning']


# In[67]:


"""
Q8. What are the three view objects in dictionaries? Use the three in-built methods in python to display
these three view objects for the given dictionary.

Ans:3 views are,1)Key,2)value,3)items

"""
dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}
dict1.keys()
#out:dict_keys(['Sport', 'Teams'])
dict1.values()
#out:dict_values(['Cricket', ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']])
dict1.items()
"""
out:dict_items([('Sport', 'Cricket'), ('Teams', ['India', 'Australia', 
'England', 'South Africa', 'Sri Lanka', 'New Zealand'])])

"""


# In[ ]:




