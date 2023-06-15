
# st = "AlgoExpert is the best!"
# out = "best1 the is AlgoExpert"

# Split or reverse methods not allowed.


#  be cognizant of the spaces. Pointer keeps moving from left to right, if space, put the space in array.
# put the values in the array . ["AlgoExpert", " ", "is", " ", "the", " ", "best!" ]
# Then somehow reverse the array

def ReverseWords(st):
    ss = st.split(" ")
    print(ss)

    # print("1 Reversed array:",ss[0].reverse())

    res = ss[::-1] #reversing using list slicing
    print("Resultant new reversed array:",res)




st = "AlgoExpert is the best!"
ReverseWords(st)

