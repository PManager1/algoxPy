#complexity is N Squared.
#question: from stephen's diagram why is he skipping the right most element on every loop ?
#it doent make sense because whats teh gurantee the first most have the correct / largest element ?
# It DOES makes sense because in each for loop it will sweet the largest number on the right most position. so you can afford to loop one less item.
# Stephen said: purpose of the Bubble sort is to find the largest element in the array and drag it on the Right most position.



def BubbleSort(ar):
    print(ar)
    for j in range(len(ar)-1):
        for i in range(len(ar)-1 -j):
            # print("i=", i); print("len(ar)=", len(ar));
            if ( ar[i] > ar[i+1]):
                swap(ar, i, i+1 );
                print("i=", i, "j=" ,j,  "ar =  ",ar)
        print(ar)

def swap(list, pos1, pos2):
    # list[pos1], list[pos2] = list[pos2], list[pos1]  #sexy way

    temp = list[pos1];
    list[pos1] = list[pos2];
    list[pos2] = temp;
    return list


ar = [8,5,2,9,5,6,3]
BubbleSort(ar)

#We stop the for loop when the last number in the list is the largest.
