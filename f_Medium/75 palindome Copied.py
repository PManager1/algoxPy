
def longestPalindrome(self, s):
    longest_palindrom = ''
    dp = [[0]*len(s) for _ in range(len(s))]
    #filling out the diagonal by 1
    for i in range(len(s)):
        dp[i][i] = True
        longest_palindrom = s[i]

    # filling the dp table
    for i in range(len(s)-1,-1,-1):
        # j starts from the i location : to only work on the upper side of the diagonal
        for j in range(i+1,len(s)):
            if s[i] == s[j]:  #if the chars mathces
                # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True
                #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                if j-i ==1 or dp[i+1][j-1] is True:
                    dp[i][j] = True
                    # we also need to keep track of the maximum palindrom sequence
                    if len(longest_palindrom) < len(s[i:j+1]):
                        longest_palindrom = s[i:j+1]

    return longest_palindrom






# def longestPalSubstr(str):
#
#     # Get length of input String
#     n = len(str)
#
#     # All subStrings of length 1
#     # are palindromes
#     maxLength = 1
#     start = 0
#
#     # Nested loop to mark start
#     # and end index
#     for i in range(n):
#         for j in range(i, n):
#             flag = 1
#
#             # Check palindrome
#             for k in range(0, ((j - i) // 2) + 1):
#                 if (str[i + k] != str[j - k]):
#                     flag = 0
#
#             # Palindrome
#             if (flag != 0 and (j - i + 1) > maxLength):
#                 start = i
#                 maxLength = j - i + 1
#
#
#     # Return length of LPS
#     return maxLength
#
# if __name__ == "__main__":
#     # Your code goes here
#     # s = "Hello"
#     s = "abba"
#     print(longestPalSubstr(s))
#




