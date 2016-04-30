#Classes
class calc:

    def add(x,y):
        return(x + y)

    def subtract(x,y):
        return(x - y)

    def multiply(x,y):
        return(x * y)

    def divide(x,y):
        return(x / y)

print(calc.add(5,5))
print(calc.subtract(100,43))
print(calc.multiply(4,8))
print(calc.divide(10,2))

#Raw text input from user 
#name = input("What is your name?: ")
#print('Hello',name)

#Statistics Module
import statistics

exList = [1,43,5,6,3,2,44,5,9]

x = statistics.mean(exList)
print(x)

x = statistics.mode(exList)
print(x)

#Standard Deviation
x = statistics.stdev(exList)
print(x)


"""
Better way to do it:
import statistics as s
or from statistics import *
This imports all
s.mean(exList)
mean(exList)
"""

"""
Something else you can do:
from statistics import mean as m, stdev as sd
print(m(exList))
Notice now that you don't need to
call anything and it is like you
created your own function
"""

#Lists
myList = ["apples","bananas","monkeys","chemistry","underwater basket weaving"]
for item in myList:
    print(item)

myList.append("algo")

print(myList.index("algo"))
print(myList.count("bananas"))
myList.remove(myList[myList.index("algo")])
print(myList)

myList.sort()
print(myList)

#Dictionaries (keys and values)
grades = {'Kelly':90, 'Matt':100, 'Mark':93}
print(grades['Matt'])

print(grades)
grades['Jessie'] = 92
del grades['Kelly']

print(grades)





