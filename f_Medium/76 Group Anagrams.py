# Function to Group Anagrams
# :param li: list of words
# :return: list of grouped anagrams
# https://leetcode.com/problems/group-anagrams/

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# words formed by same letters. but arranged differently.
# test_list = ['lump', 'eat',  'me',  'tea', 'em', 'plum']
# list  = ['yo', 'act',  'flop',  'tac', 'cat', 'oy', 'olfp']
# The original list : ['lump', 'eat', 'me', 'tea', 'em', 'plum']
# The grouped Anagrams : [['me', 'em'], ['lump', 'plum'], ['eat', 'tea']]
# BF :  take one adn compare it with the Reverse of the string. See if it equals.

'''
def groupAnagrams(words):
    print(words)
    pass






test_list = ['lump', 'eat',  'me',  'tea', 'em', 'plum']
groupAnagrams(test_list)
'''


'''

from collections import defaultdict
# initializing list
test_list = ['lump', 'eat',  'me',  'tea', 'em', 'plum']

# printing original list
print("The original list : " + str(test_list))   # print("The original list : ",  test_list)

# Grouping Anagrams
temp = defaultdict(list)   # temp = {}
print("42 temp : " , temp)
for ele in test_list:
    print("===> 44 ele : " , ele, "61 sorted(ele) : ", sorted(ele))
    temp[str(sorted(ele))].append(ele) # this is the IF statement
    print("===> 46 temp : ", temp)
res = list(temp.values())

# print result
print("The grouped Anagrams : " , str(res))

'''
# Best solution from Algoexpert video


def groupAnagrams(words):
    anagrams = {}
    for word in words:
        print(word)
        sortedWord = "".join(sorted(word))
        print("60-sortedWord =", sortedWord)
        # sortedWord2 =  sorted(word)
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word) # Its already there , now inserting more values in it.
            print(" Found word in anagrams =", sortedWord, anagrams)
        else:
            anagrams[sortedWord] = [word] # Creating for the first time.
            print("Else Insert in the dictionary - anagrams =", sortedWord ,  anagrams)
    print( anagrams.items())
    # res =list(anagrams.values())
    res = anagrams.values()
    print("The grouped Anagrams : " + str(res))
    return res;

# list  = ['lump', 'eat',  'me',  'tea', 'em', 'plum']
list  = ['yo', 'act',  'flop',  'tac', 'cat', 'oy', 'olfp']
val  = groupAnagrams(list)
print("The grouped Anagrams : " + str(val))




