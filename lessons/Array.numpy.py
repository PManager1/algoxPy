import numpy as np

# Adding multipel arrays into single array .

x = np.array([2, 3])
y = np.array([4, 5])
print ("np stack =", np.stack((x, y))  )

# array1 = []
array1 = np.stack((x, y))

print ("np array1 =", array1)