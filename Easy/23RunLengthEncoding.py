# https://github.com/pinglu85/algoExpert/blob/main/Easy/run-length-encoding.md

# Given a non-empty string, we are asked to write a function that is going to run-length-encode the input string
# and return the encoded string.
# Run-length encoding refers to   ***** replacing repetitive ****** , consecutive data by a count and one copy of a repeated data.
# For instance, AAABB will be encoded as 3A2B


# If a sequence contains more than 9 consecutive, identical characters, we first encode 9 characters,
# then the remaining ones.
# For instance, AAAAAAAAAA (10 As) will be encode as 9A1A.
# 9A4A2B4C2D


# > Eliminate the use of many If Else cases.  Use as less as possible.
#
# First figure out which condition is like default  i.e  is going to be obstructed So use that in the IF condition,  Not for every Fucking case.
# > Figure the unique cases where a lot of stuff gets changed, Vs where nothing is being changed.
#
# st = "AAAAAAAAAAAAABBCCCCDD"
# Here large case has same characters, so use that as default & if case only when the code breaks.
#

def  runLengthEncoding(st):
    # print(st)


    currentLen=1;
    chars = []
    for i in range (1, len(st)):
        currentCh = st[i];
        prevCh = st[i-1];
        print("equal = st[i]=",  st[i-1], st[i])

        if(currentCh != prevCh or currentLen == 9):
          chars.append(str(currentLen))
          chars.append(prevCh)
          print("29-chars=", chars)
          currentLen = 0;

        currentLen +=1
    chars.append(str(currentLen))
    chars.append(prevCh)
    print("33-chars=", chars)
    res = "".join(chars)
    print("res=", res)
    return res
    # print("23-currentLen =", currentLen, "currentCh=", currentCh )

# count the number of AAAA s
# Do in notebook first
# 13A 2B 4C 2D
# 9A4A2B4C2D

st = "AAAAAAAAAAAAABBCCCCDD"
runLengthEncoding(st)