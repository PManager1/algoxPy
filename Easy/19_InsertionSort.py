# 239PM
# [2, 5, 5, 8, 6, 9, 3]
# status : not working.

def swap( ar, p1, p2 ):
    print("6-swap ar, p1, p2 =",  ar, p1, p2)
    # ar[p2], ar[p1] = ar[p1], ar[p2]
    ar[p1], ar[p2] = ar[p2], ar[p1]
    print("      swapped arr =", ar)
    return ar

def insertionSort(ar):
    print("12ar=", ar)
    for i in range(1, len(ar)):
        print("i =", i, "ar[j] =", ar[i],   "len =" , len(ar))

        j = i;
        while ( j>0  and  ar[j-1] > ar[j] ):
          swap( ar, j-1, j )
          j-=1

ar = [8,5,2,9,5,6,3];
insertionSort(ar)