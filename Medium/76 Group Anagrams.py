# Function to Group Anagrams
# :param li: list of words
# :return: list of grouped anagrams

# https://leetcode.com/problems/group-anagrams/

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# words formed by same letters. but arranged differently.

# test_list = ['lump', 'eat',  'me',  'tea', 'em', 'plum']
#
# The original list : ['lump', 'eat', 'me', 'tea', 'em', 'plum']
#
# The grouped Anagrams : [['me', 'em'], ['lump', 'plum'], ['eat', 'tea']]
#
# BF :  take one adn compare it with the Reverse of the string. See if it equals.
#
