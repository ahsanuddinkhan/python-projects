Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#how to use slice operator to copy objects from a list and thereby creating 2 lists
>>> list1=[12,'alpha','omega',3.14] # here we have created list1 with 4 objects
>>> list2=list1[:]  #here we are copying objects from list1 to list2
>>> print(id(list2),id(list1))
2482152519104 2482152520896 #By using the id function we can easily identify that both lists have different addresses in memory
>>> list2[0]=1 #change value of 1st object in list2
>>> print(list1)
[12, 'alpha', 'omega', 3.14]  #we see that list1 is still unchanged
>>> print(list2)
[1, 'alpha', 'omega', 3.14]   #here we see that list2 has it's first element changed
