# https://leetcode.com/problems/monotonic-array/

# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
#
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

# Input: nums = [1,2,2,3]
# Output: true

# Input: nums = [6,5,4,4]
# Output: true

# Input: nums = [1,3,2]
# Output: false
def checkAscArr(ar):
    for i in range(1,len(ar)-1):
        print("i=", i)
        if ar[i] <= ar [i+1]:
            continue;
        else:
            return False

    return True;

def checkDescArr(ar):
    for i in range(1,len(ar)-1):
        print("i=", i)
        if ar[i] >= ar [i+1]:
            continue;
        else:
            return False

    return True;


# Condition if the first two elements are same ?  Use for loop to Compute the direction here first, it has to has a direction.
def Ismonotonic(ar):
    print(ar)
    i=0
    if ar[i] < ar[i+1]:
      res = checkAscArr(ar)
    else:
      res = checkDescArr(ar)

    return res



# ar = [1,2,2,3]
# ar = [6,5,4,4]
ar = [1,3,2]
out = Ismonotonic(ar)
print("out= ", out )