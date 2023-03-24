# string_to_hex_utf8.py

# convert the string to the bytes

str = 'AE123456D0A1'.encode('utf-8')

# print the converted string to bytes

print(str)

# convert the string bytes to the hexadecimal string

hex_str = str.hex()



# print the converted hexadecimal value type

print(hex_str)


# Python 3 code to demonstrate the
# working of MD5 (string - hexadecimal)

import hashlib

# initializing string
hexstr = "AE123456D0A1"

bytesstr = bytes.fromhex(hexstr)


# encoding GeeksforGeeks using encode()
# then sending to md5()
result = hashlib.md5(bytesstr)

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end ="")

print(result.hexdigest())

