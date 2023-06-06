# 239PM
def insertionSort(ar):
    print(ar)
    for j in range(len(ar)):
        print("j =" , j, ar[j], "len =" , len(ar))
        for i in range(j):
            # here we do the swaping
            print("j in=" , j)
            print("8 ar[j] =",  ar[j])

def swap(arr, p1,p2):
    temp = p1
    p1 = p2
    p2=temp
    return arr


ar = [8,5,2,9,5,6,3];
insertionSort(ar)