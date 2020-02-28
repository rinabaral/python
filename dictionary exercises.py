"""Question 1: Below are the two lists convert it into the dictionary"""
keys = ['Hello', 'How', 'you']
values = ['Sana', 'are', '?']

dictionary=dict(zip(keys, values))
print(dictionary)

"""Question 2: Merge following two Python dictionaries into one"""
dict1 = {'Hi': 12, 'Are': 20, 'You': 30}
dict2 = {'Hey': 34, 'You': 40, 'Fine': 50}

dict3 =dict1.copy()
dict3.update(dict2)
print(dict3)

"""Question 3: Access the value of key ‘history’"""
sampleDict = { 
   "class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
print(sampleDict['class']['student']['marks']['history'])


"""Question 4: Initialize dictionary with default values"""
employees = ['Jova', 'Elson', 'John']
defaults = {'Application Developer', 6000}
print(dict.fromkeys(employees, defaults))

"""Question 5: Create a new dictionary by extracting following keys name and salary
from a given dictionary"""
 
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}

new = {key: sampleDict[key] for key in sampleDict.keys()& {'name', 'salary'}}
print("The new dictionary is :", str(new))

"""6: Delete set of keys from Python Dictionary"""
#lets use the dictionary of question 5

toremove = {key: sampleDict[key] for key in sampleDict.keys()- {'name', 'salary'}}
print("The new dictionary with keys removed :", str(toremove))

"""Question 7: Check if a value 200 exists in a dictionary"""
Dict = {'a': 100, 'b': 200, 'c': 300}
print(200 in Dict.values())

"""Question 8: Rename key city to location in the following dictionary"""
Dict1 = {
  "name": "John",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
Dict1['location'] = Dict1.pop('city')
print(Dict1)

"""Question 9: Get the key corresponding to the minimum value from the following dictionary"""
Subject = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(min(Subject, key=Subject.get))

"""Question 10: Given a Python dictionary, Change Brad’s salary to 8500"""
Employees = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}
Employees['emp3']['salary']= 8500
print(Employees)
      








