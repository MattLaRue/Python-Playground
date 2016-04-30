#Printing
print('#Printing')
print('Hello World\n')

#Math
print('#Math')
print('What is 2 + 2?', 2+2 ,'\n')

#variables
var = 100
print('#Varibles - var =',var)
print(var)
print(var / 20,'\n')

print()

#variable with number
_100 = 100

#While Loops
condition = 1
print('#While Loops')
while condition <= 10:
    print(condition)
    condition+=1

print()

#For Loop
print('#For Loops')
exampleList = [1,2,3,4,5,6]
for thing in exampleList:
    print(thing)

print()

#If/Else/Elif Statements
x = 2
y = 7
z = 10

print('#If/Elif/Else')
if x < y: 
    print(x, 'is less than',y)
elif x == y:
    print(x,'is equal to',y)
else:
    print(x,'is greater than y',y)

print()

#Functions
def example():
    print ('Hello World')

print('#Functions')
example()
print()

#You can call functions inside of functions
"""
def main():
    example()
"""

#Parameters
def add(num, num2):
    return num + num2
print('#Functions with parameters')
print(add(1,2))

print()

#Global and local variables
x = 6

print('#Global/Local')
def accessX():
    z = 5
    print(z)
#Can't do this:
    #print(z)
#Or this:
    #x+=1
    #print(x)

#To access the global x:
    global x
    x+=1
    print(x)

"""However, this is not the preferred method,
    it is better to take the global variable
    and put it into a new variable
         Ex: y = x
"""

accessX()

