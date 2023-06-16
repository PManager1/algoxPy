# Given a string s, return the longest  palindromic
#
# substring in s.
# Example 1:

# Input: st = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"

def getPalindrome(st, leftIdx, rightIdx):
    print("15-calling getPalindrome", leftIdx, st[leftIdx],  rightIdx, st[rightIdx])
    # Return the pointers , &  Return the difference between the left & right,
    while ( leftIdx >= 0 and rightIdx < len(st)):
        print("18-inside while", leftIdx, st[leftIdx],  rightIdx, st[rightIdx])
        if ( st[leftIdx] != st[rightIdx] ):
            print("20 Not Equal pointers", leftIdx, st[leftIdx],  rightIdx, st[rightIdx])
            return [leftIdx, rightIdx]
            break
        print("22 Incrementing the left and right pointers")
        leftIdx -=1         #correct -1 becuase you are expanding to left  and right.
        rightIdx+=1
        print("before equal pointers return=", leftIdx, st[leftIdx],  rightIdx, st[rightIdx])
        return [leftIdx, rightIdx]

def longestPalindomre(st):
    longestPalin = 2;
    pointers = [0,1]  # Why
    # isEven, isOdd
    if len(st) %2 == 0 : print("is even");  isEven = True #|| print("is even");   # odd = getPalindrome()
    if len(st) %2 != 0: print("is Odd");  isOdd = True

    currentLongest = [0,1]
    for i in range(1,len(st)):
        print("38--i, st[i]=", i, st[i]);
        # if ( isOdd):
        #     odd = getPalindrome(st, i-1, i+1 )  # 1,2 | 2,3 | 3,4 | 4,5
        #     print("odd=", odd)
        if ( isEven ):
            value = getPalindrome(st, i-1, i )  # 0,1 | 1,2 | 2,3 | 3,4
            print("returned=", value)
            difference = value[1] - value[0]
            print("difference=", difference)
            if difference > longestPalin:
                longestPalin = difference
                pointers = value
                print("50-value =", value)
    return pointers
        # Get the difference between the left & right which is the length of the palindrome.
#         Grab the longest returned palidorme , update the value in currentLongest and return.
# st = "abcba"
st = "abba"
res = longestPalindomre(st)
print("57-longestPalindomre  res = ", res)