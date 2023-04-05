from hex_to_bytes import mac_list_to_md5

mac_list = ['ae:12:34:56:d0:a1',
                'df:2f:11:87:4f:f7',
                'db:55:a6:9d:0b:b4']

print(mac_list_to_md5(mac_list))