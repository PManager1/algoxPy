# Write a function that takes in an array of integers and returns an array of the same length,
# where each element in the output array is equal to the product of every other number in the input array.

# inputArr = [5,1,4,2];
# outputArr = [8,40,10,20];


def arrayOfProucts(ar):
    resultsAr=[]
    for item in ar:
        copyArr = ar.copy();
        copyArr.remove(item); print("copyArr=" , copyArr)

        mulOfThree = 1
        for el in copyArr:
            print("15-copyArr=" , copyArr)
            mulOfThree *=el;


        print("mulOfThree=" , mulOfThree)
        resultsAr = resultsAr + [mulOfThree]
        print("20-resultsAr=====" , resultsAr)

    return resultsAr


inputArr = [5,1,4,2]
print("arrayOfProucts(inputArr) = ", arrayOfProucts(inputArr))
