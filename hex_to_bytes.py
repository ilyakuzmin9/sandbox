import hashlib
# # string_to_hex_utf8.py
# # convert the string to the bytes
# str = 'AE123456D0A1'.encode('utf-8')
# # print the converted string to bytes
# print(str)
# # convert the string bytes to the hexadecimal string
# hex_str = str.hex()
# # print the converted hexadecimal value type
# print(hex_str)
# # Python 3 code to demonstrate the
# # working of MD5 (string - hexadecimal)
#
# # initializing string
# hexstr = "AE123456D0A1"
# bytesstr = bytes.fromhex(hexstr)
# # encoding GeeksforGeeks using encode()
# # then sending to md5()
# result = hashlib.md5(bytesstr)
# # printing the equivalent hexadecimal value.
# print("The hexadecimal equivalent of hash is : ", end ="")
# print(result.hexdigest())

def mac_list_to_md5(a_mac_list):
    hash_mac_list = []
    for mac in a_mac_list:
        mac = mac.replace(':','')
        bytes_mac = bytes.fromhex(mac)
        hash_mac = hashlib.md5(bytes_mac)
        hash_mac_list.append(hash_mac.hexdigest())
    return hash_mac_list

# mac_list = ['ae:12:34:56:d0:a1',
#             'df:2f:11:87:4f:f7',
#             'db:55:a6:9d:0b:b4',
#             '5e:17:72:85:6f:89',
#             '8e:58:26:eb:0a:4c',
#             '13:f2:76:8a:f0:79',
#             '56:25:46:92:dd:15',
#             '82:56:72:3b:f8:50',
#             'd4:1a:e5:b7:f4:d0',
#             '8b:c1:bf:0e:f4:1f',
#             'b2:85:6f:bc:49:09']
#
# print(mac_list_to_md5(mac_list))

