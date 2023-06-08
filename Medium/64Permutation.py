def swap(ar):
    # print("swap called bef ar =" , ar )
    ar[0], ar[1]= ar[1], ar[0]
    # print("swap after ar =" , ar )
    return ar;


def doWork(ar):
    allPerms =[];
    for item in ar:
        print("========================iteration item=", item)
        ar1 = ar.copy()
        ar1.remove(item);           # print("ar1=", ar1)
        first = [item]+ ar1;         print("15-first =",   first);
        sec = [item]+ swap(ar1);     print("18-sec =",   sec);
        allPerms.extend(first)
        allPerms.extend(sec)
        print("18========================allPerms=", allPerms)
    return


ar1 = [1,2, 3]
doWork(ar1)