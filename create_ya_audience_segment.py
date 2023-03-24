import requests

url = "https://api-audience.yandex.ru/v1/management/segments/upload_csv_file"

# Replace the filename with the name of the CSV file you want to send
filename = "example.csv"

# Open the CSV file and read its contents
with open(filename, "rb") as file:
    csv_data = file.read()

# Set the headers for the request
headers = {"Content-Type": "text/csv"}

# Send the HTTP POST request with the CSV data in the body
response = requests.post(url, headers=headers, data=csv_data)

# Print the response from the server
print(response.text)
