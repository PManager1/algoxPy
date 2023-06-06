# 239PM
# [2, 5, 5, 8, 6, 9, 3]
# status : not working.
def insertionSort(ar):
    print(ar)
    for j in range(1, len(ar)):
        print("j =" , j, ar[j], "len =" , len(ar))
        for i in range(j):
            # here we do the swaping
            print("9=== j =" , j)
            print("10-> ar =", ar, "j =" , j, " i =", i , "ar[i-1]= ", ar[i], "ar[i] =", ar[i+1]  )
            if  ( ar[i] > ar[i+1] ):  swap ( ar, i,i+1 )

            print("13- ar[j] =",  ar[j])

def swap(arr, p1,p2):
    arr[p1], arr[p2] = arr[p2], arr[p1]
    print("swapped arr =", arr)
    return arr

ar = [8,5,2,9,5,6,3];
insertionSort(ar)