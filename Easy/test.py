def my_function():
    print("Hello from a function")

my_function()


b = "Hello, World!"
print(b[2:5])

a = "Hello, World!"
print(a.upper())


thislist = ["apple", "banana", "cherry"]
print(thislist)

cars = ["Ford", "Volvo", "BMW"]
print(cars)

for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#set
thisset = {"apple", "banana", "cherry"}
print(thisset)

