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