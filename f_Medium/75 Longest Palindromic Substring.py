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


def longestPalindomre(st):
    for idx, ch in range(1,len(st)):
      print(idx)
      print(ch)




# st = "abcba"
st = "abba"
longestPalindomre(st)