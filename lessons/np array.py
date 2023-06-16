import numpy as np

#Create NumPy arrays
arr = np.array([4, 7, 12])
arr1 = np.array([5, 9, 15])

con = np.concatenate((arr, arr1), axis=1)
print(con)


'''
con = np.concatenate((arr, arr1))
print(con)

# Example 2: Use concatenate() with axis
con1 = np.concatenate((arr, arr1), axis=1)
print(con1)

# Example 3: Use np.stack() function to Join Arrays
con2 = np.stack((arr, arr1), axis=1)
print(con2)

# Example 4: Use np.hstack() function
con3 = np.hstack((arr, arr1))
print(con3)

# Example 5: Use np.vstack() function
con4 = np.vstack((arr, arr1))
print(con4)

# Example 6: Use np.dstack() function to Stacking Along Height (depth)
con5 = np.dstack((arr, arr1))
print(con5)
'''