str1 = "Hello,Everyone,Welcome,to,Tutorialspoint"

print("The given CSV string is")
print(str1)
test = str1.split(',')
print("test =", test)

print("Converting the given CSV string into array")
res = list(map(str.strip, str1.split(',')))
print("res=",res)
