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

def groupAnagrams(words):
    anagrams = {}

    for el in words:
        print("el =", el)
        print("21-sorted(el =", sorted(el) )
        sortedword2 = sorted(el)
        print("23-sortedword2 =", sortedword2 )

        sortedword ="".join(sorted(el))
        print("26-sortedword2 =", sortedword )

        print("25-anagrams =", anagrams )
        if sortedword in anagrams:
            print("yes inside")
            anagrams[sortedword].append(el) # Its already there , now inserting more values in it.
        else:
            print("Not inside")
            anagrams[sortedword] = [el]  # Creating for the first time.

    print("anagrams = ", anagrams)



list  = ['yo', 'act',  'flop',  'tac', 'cat', 'oy', 'olfp']
groupAnagrams(list)
# val  = groupAnagrams(list)

# print("The grouped Anagrams : " + str(val))




