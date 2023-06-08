import numpy as np

# Need :  the allPerms should take all the arrays in stacks.
def swap(ar):
    # print("swap called bef ar =" , ar )
    ar[0], ar[1]= ar[1], ar[0]
    # print("swap after ar =" , ar )
    return ar;

# np.array([2, 3, 4])

def doWork(ar, allPerms):

    for item in ar:
        # print("========================iteration item=", item )
        print("========================iteration item=", item ,  "allPerms =", allPerms)

        ar1 = ar.copy()
        ar1.remove(item);           # print("ar1=", ar1)
        first = [item]+ ar1;         print("16-first =",   first , np.array(first) );
        sec = [item]+ swap(ar1);     print("17-sec =",   sec, np.array(sec));
        allPerms = np.stack((first, sec));
        # print("18========================allPerms=",  allPerms=np.stack((first, sec))  )
        print("21====allPerms=", allPerms )

    return


ar1 = [1,2, 3]
allPerms =[];
doWork(ar1, allPerms)