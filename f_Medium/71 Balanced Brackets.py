
leftBraket = '(' or '{' or '[';

rigtBraket = ')' or '}' or ']';

string = '(([]()()){})';

stack = [];
matchingBrackets  = { ')': '(', '{': '}', '[': ']' }


for char in string:
    print("char =", char )

#   if the next bracket is leftBraket put it in the stack.
#     if the next bracket is rightBraket put it in the stack., check the last element in the stack, if its a (1) match, Throw it away.
#   Keep diong it until it reaches the stack empty, if not Return False.

# (1)  How do check match ? [ with ]    or  { with }   or  ( with ) using the matchingBrackets

# Check if its an opening bracket

