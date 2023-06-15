# You are given an array of integers and an integer. Write a function that moves all
# instances of that integer in the array to the end of the array. Return the array.

# The function should mutate the input array, (using same array,  )
# i.e. the operation should be performed in place,
# and doesn’t need to maintain the order of the integers.

#input = [2,1,2,2,2,3,4,2]; // 2
#out = [1,3,4,2,2,2,2,2];  we dont care abt the order of the other numbers, only the 2s shoudl be at the last.

def swap(ar,a,b):
    print("swap fn called Left =", a, "Right = ", b,  ar)
    ar[a], ar[b] = ar[b], ar[a]
    print("14-after swap  ar                =",  ar)
    return


def moveElement(ar,toMove):
    Left =0; Right = len(ar)-1
    while Left< Right:

        while Left < Right and ar[Right] == toMove:
            Right -=1        # Keep moving the pointer to the Left until U keep finding 2.
            print("24-ar(Right) == toMove Left=", Left, "ar[Left]=", ar[Left], "Right=", Right, "ar[Right]=", ar[Right] )

        if ar[Left] == toMove: # When the left find the 2 you swap.
            print("28: Calling swap()  Left =", Left, "Right = ", Right)
            swap(ar,Left,Right)
            Left += 1;
        if ar[Left] != toMove:
            print("31-ar(Left) != 2")
            Left = Left+1;

        print("34- Left=", Left, "ar[Left]=", ar[Left], "Right=", Right, "ar[Right]=", ar[Right], "ar=", ar )




ar =[2,1,2,2,2,3,4,2];
moveElement(ar,2)