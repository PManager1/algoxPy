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

def getPalindrome():
    print("calling getPalindrome")
    # Return the difference between the left & right which is the length of the palindrome.


def longestPalindomre(st):

    # isEven, isOdd
    if len(st) %2 == 0 : print("is even");  isEven = True #|| print("is even");   # odd = getPalindrome()
    if len(st) %2 != 0: print("is Odd");  isOdd = True

    currentLongest = [0,1]
    for i in range(1,len(st)):
        print("i, st[i]=", i, st[i]);
        odd = getPalindrome( i-1, i+1 )  # 1,2 | 2,3 | 3,4 | 4,5
        even = getPalindrome( i-1, i )  # 0,1 | 1,2 | 2,3 | 3,4
        # Get the difference between the left & right which is the length of the palindrome.
#         Grab the longest returned palidorme , update the value in currentLongest and return.


# st = "abcba"
st = "abba"
longestPalindomre(st)