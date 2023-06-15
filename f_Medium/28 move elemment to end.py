# You are given an array of integers and an integer. Write a function that moves all
# instances of that integer in the array to the end of the array. Return the array.

# The function should mutate the input array, (using same array,  )
# i.e. the operation should be performed in place,
# and doesn’t need to maintain the order of the integers.

#input = [2,1,2,2,2,3,4,2]; // 2
#out = [1,3,4,2,2,2,2,2];  we dont care abt the order of the other numbers, only the 2s shoudl be at the last.

def swap(ar,a,b):
    print('swap fn called')
    ar[a], ar[b] = ar[b], ar[a]
    print('14-after swap called ar=', ar)
    return


def moveElement(ar,toMove):
    Left =0; Right = len(ar)-1
    while Left< Right:

        while ar[Right] == toMove:
            print("22-ar(Right) == toMove Right=", Right)
            Right -=1
            print("24-ar(Right) == toMove Right=", Right, "ar[Right]=", ar[Right] )
        if ar[Left] == toMove:
            print("swap()")
            swap(ar,Left,Right)
            Left = Left+1;
        if ar[Left] != toMove:
            print("ar(Left) != 2")
            Left = Left+1;





ar =[2,1,2,2,2,3,4,2];
moveElement(ar,2)