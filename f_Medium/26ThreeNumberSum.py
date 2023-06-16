
# I’m talking about the sexual stuff with you, why aren’t you getting offended by me Gina ?
# Input: nums = [-1,0,1,2,-1,-4] //0
# Output: [[-1,-1,2],[-1,0,1]]

# input  = [12,3,1,2,-6,5,-8,6] // 0      [-8, -6, 1, 2, 3, 5, 6, 12]
# out = [[-8,2,6] [-8,3,5] [-6,1,5]]


def threeNumSum(ar, length, target):
    triplates= []
    ar.sort(); print("11-ar=" ,  ar, "len(ar)-1 =", len(ar)-1);
    # print("len(ar)-2 =", len(ar)-2)
    for i in range(0, len(ar)-1 ):
    # for i in range(len(ar) - 2):
        print("ar[i] =", ar[i] )
        leftIdx = i+1
        rightIdx= len(ar) - 1

        while (leftIdx < rightIdx ):
            sum =  ar[i] + ar[leftIdx] + ar[rightIdx]
            print("22- i=", i, "leftIdx=", leftIdx, ar[leftIdx],  "rightIdx=", rightIdx, ar[rightIdx] , "sum=", sum,  "triplates=",triplates)

            if sum == target:
                print("25:sum == target")
                triplates.append(ar[i])
                triplates.append(ar[leftIdx])
                triplates.append(ar[rightIdx])
                leftIdx +=1; rightIdx-=1
                print("27:triplates=", triplates)
            elif sum > target:
                print("29:sum > target")
                rightIdx -=1;
            elif sum < target:
                print("32:sum < target")
                leftIdx +=1;


ar = [12,3,1,2,-6,5,-8,6]  #ar = [12,3,1,2,-6,5,-8,6]
target = 0 ; length = len(ar)
threeNumSum(ar,length, target)