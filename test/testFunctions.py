'''
def passArr(ar):
    ar.append(23)
    ar.append('Engineering')
    ar.insert(0, 'First')
    testFn(ar)


def testFn(ar):
    print(ar)
    ar.pop()
    print(ar)


ar = [8,5,2,9,5,6,3]
passArr(ar)

'''


def swapPositions(list, pos1, pos2):
    temp = list[pos1];  print(temp)
    list[pos1] = list[pos2]; print("23list", list)
    list[pos2] = temp; print("24list", list)

    # list[pos1], list[pos2] = list[pos2], list[pos1]  #sexy way
    return list

# Driver function
List = [1, 2, 3, 4]
pos1, pos2  = 1, 3

print(swapPositions(List, pos1-1, pos2-1))