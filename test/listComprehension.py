ar = [1,2,3,4,5]
for item in ar:
    print(item)
    # print(ar[item])

for i in range(len(ar)):
    print("i=",i)

#list comprehension.  for loop inside a list
x = [i for i in range(10)]
print(x)


def complicateFn(x,y):
    print(x,y)

complicateFn(y=2, x=1);


def optionalParameterFn(x,y=None ):  #y isnt' required to pass any value.
    print(x,y)
optionalParameterFn( x=1);


# **kwargs  we accept any no of keyword arguments.
def newFn(*args, **kwargs ):  #y isnt' required to pass any value.
    print("args=",args, kwargs["x"])
    pass

newFn( x=1, y=3 );