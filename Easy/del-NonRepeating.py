def FirstNonRepeating(A):
    # Code here
    list = []
    mp = {}
    ans = ''

    for ch in A:
        if ch not in mp:  # new character visited first time
            print("list=", list)
            list.append(ch)
            print("mp1=", mp)
            mp[ch] = 1
            print("mp=", mp)
        else:
            # any repeated character encountered
            if ch in list:
                list.remove(ch)
        ans += list[0] if list else '#'

    return ans
# l = "geeksforgeeksandgeeksquizfor"
l = "abcdcaf"
ans1 = FirstNonRepeating(l)
print(ans1)