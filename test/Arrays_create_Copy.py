a = [1,2,3]
b = [4,5,6]
print("a+b =", a+b)

print("[9]+a =", [9]+a)
print("a+[9] =", a+[9])


# Remove a specific element from an array.
ar3 = [1,2, 3, 4]
print("ar3 =", ar3)
ar3.remove(4) # you just put that number and it will be removed.
print("ar3 =", ar3)



# creating the first array
arr1 = [1,2, 3, 4]

# displaying the identity of arr1

# assigning arr1 to arr2
arr2 = arr1.copy()
# displaying the identity of arr2
print(arr1)
print(arr2)

# making a change in arr1
arr1.pop()
# displaying the arrays
print("arr1 =", arr1)
print("arr2 =", arr2)


