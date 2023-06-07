def FirstNonRepeating(A):
    list = [] # keep track of non repeating elements.
    mp = {} # map when it contains the elements.

    for ch in A:
        if ( ch not in mp ): #not in teh map
            mp[ch] = 1;    #ddd to the map
            list.append(ch)
        else:
            list.remove(ch)
    print("final list=", list)

l = "abcdcaf"
ans1 = FirstNonRepeating(l)
print(ans1)



''' peeked online 
def FirstNonRepeating(A):
    # Code here
    list = []  #will keep track of all the items.  If repeated here, it will pop/ remove it.
    # So only the chars that are non repeating.
    mp = {}
    ans = ''

    for ch in A:
        if ch not in mp:  # new character visited first time
            print("ch=", ch); print("list=", list)
            list.append(ch) #inserting into the list.
            print("mp1=", mp)
            mp[ch] = 1
            print("mp=", mp)
        else:
            # if Repeated character encountered
            if ch in list:  #keeping track of items in the list/ array.
                list.remove(ch)

    return ans

l = "abcdcaf"
ans1 = FirstNonRepeating(l)
print(ans1)
'''