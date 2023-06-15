# Given a string queryIP, return "IPv4" if IP is a valid IPv4 address,
# "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.
#
# A valid IPv4 address is an IP in the form "x1.x2.x3.x4"
# where 0 <= xi <= 255 and xi cannot contain leading zeros.
#
# For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses
# while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.
#
# A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
# 1 <= xi.length <= 4
# xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
# Leading zeros are allowed in xi.

# ?  https://www.geeksforgeeks.org/program-generate-possible-valid-ip-addresses-given-string/

# Constraints:
# queryIP consists only of English letters, digits and the characters '.' and ':'

# no leading zeros
# It can be from 0 to 255
# It can't go over 12 digits.
# can't have no loading zeros, so the minimum number you can create is :  1000


# Solution is to try all of the 4 valid values inside the periods.


