import requests
from create_random_mac_list import write_list_to_csv, generate_mac_list
from hex_to_bytes import mac_list_to_md5

mac_list = generate_mac_list(100)
hashed_mac_list = mac_list_to_md5(mac_list)
output_file = 'output_files/random_mac_list.csv'
write_list_to_csv(output_file, hashed_mac_list)





# url = "https://api-audience.yandex.ru/v1/management/segments/upload_csv_file"
#
# # Replace the filename with the name of the CSV file you want to send
# filename = "example.csv"
#
# # Open the CSV file and read its contents
# with open(filename, "rb") as file:
#     csv_data = file.read()
#
# # Set the headers for the request
# headers = {"Content-Type": "text/csv"}
#
# # Send the HTTP POST request with the CSV data in the body
# response = requests.post(url, headers=headers, data=csv_data)
#
# # Print the response from the server
# print(response.text)
