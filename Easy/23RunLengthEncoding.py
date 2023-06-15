# Given a non-empty string, we are asked to write a function that is going to run-length-encode the input string
# and return the encoded string.
# Run-length encoding refers to replacing repetitive, consecutive data by a count and one copy of a repeated data.
# For instance, AAABB will be encoded as 3A2B

# If a sequence contains more than 9 consecutive, identical characters, we first encode 9 characters,
# then the remaining ones.
# For instance, AAAAAAAAAA (10 As) will be encode as 9A1A.
# 9A4A2B4C2D
def  runLengthEncoding(st):
    # print(st)

    currentCh = "";
    currentMax=0;
    chars = []
    for i, val in enumerate(st):
        print(i, val)
        if(st[i] == st[i+1]):
            print("equal = st[i]=", st[i], i , i+1)
            currentCh = st[i];
            currentMax +=1
        else:
            print("23-currentMax =", currentMax, "currentCh=", currentCh )
            # print("24-list=", list)
            list = str(currentMax) + currentCh
            print("26-list=", list)
            chars.append(list)
            currentMax = 0;
            currentCh= st[i+1]
            print("30-chars=", chars)


# count the number of AAAA s
# Do in notebook first


st = "AAAAAAAAAAAAABBCCCCDD"
runLengthEncoding(st)