def swap(ar):
    print("swap bef ar =" , ar )
    ar[0], ar[1]= ar[1], ar[0]
    print("swap after ar =" , ar )


def doWork(ar):
    for val in ar:
        print(val)

    ar1 = ar.copy()
    ar1.remove(val)
    print("ar1=", ar1)
    # take the two elemnts of ar1.
    swap(ar1)  # swap the 2 elmenets of ar1.
    return


ar1 = [1,2, 3]
doWork(ar1)