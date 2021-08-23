#!/usr/bin/env python
# coding: utf-8

# In[2]:


menu=["osh", "samosa", "manti", "shavla", "dolma", "soup", 'mastava'] # "Uzbek cuisines"
food=input("What would you like to eat?\n>>>")
if food.lower() in menu:
    print("The order accepted.")
else:
    print("So sorry, we dont have this food at present.")


# In[6]:


#DICTIONARY
cars={'model': "toyota", "color": "red"}
print(cars['model'].title())
print(cars['color'].title())


# In[7]:


#adding items
cars["price"]=4000
cars["year"]=2019
print(cars)


# In[8]:


#changing items
cars["price"]=5000
#deleting items
del cars["year"]
print(cars)


# In[14]:


phones={
    'ali': 'nokia',
    'vali': 'Samsung S9',
    'john': 'iphone8',
    'temur':'Note 10+',
    'Bill': 'Samsung S9'

}
for k, v in phones.items():
    print(f" {k.title()} uses {v.title()}.")


# In[15]:


print(phones.keys())
print(phones.values())


# In[16]:


for phone in set(phones.values()):   #set is used not repeat th same values

    print(phone)


# In[17]:


#NESTING
car0={
    'model': "lacetti",
    'color': "white",
    "year": 2019,
    "price": 13000
}

car1={
    "model": "Nexia3",
    "color": "black",
    "year": 2015,
    "price": 9000
}

car2={
    "model": "gentra",
    "color": "red",
    "year": 2019,
    "price": 20_000
}
cars=[car0, car1, car2]
for car in cars:
    print(f"{car['color'].title()} {car['model'].title()} was produced in {car['year']} and its price is {car['price']}." )

