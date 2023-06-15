
# Write a function that takes in an array of integers and returns an array of length 2 representing
# the largest range of numbers contained in that array. The rst number in the output array
# should be the rst number in the range while the second number should be the last number
# in the range. A range of numbers is dened as a set of numbers that come right after each other
# in the set of real integers. For instance, the output array [2, 6] represents the range
# {2, 3, 4, 5, 6}, which is a range of length 5. Note that numbers do not need to be ordered or
# adjacent in the array in order to form a range. Assume that there will only be one largest range.

# Sample input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6] Sample output: [0, 7]



#  You cant sort the array

# insert all nos in the set  with : True as key value.
# start iteraritn from left to right as you explore the nos,

# start with first no which is 1 & check if the nos smaller than 1 are in the table. i.e 0,  first go backwards & then forwards.

# As the nos comem in the range, you put a flag false next to it.


# [1,11,3,0,15,5,2,4,10,7,12,6]


15:30