import json
import csv

json_name = 'input_files/1chr/response-jan-Trafic-f1.json'
json_file = open(json_name)
read_file = json.loads(json_file.read())

data_list = [item for item in read_file]

print(data_list)

output_csv =f"output_files/1chr/{json_name.replace('input_files/1chr/', '').replace('.json', '')}.csv"

with open(output_csv, 'w', newline='') as csvfile:
    fields = data_list[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

    for elem in data_list:
        writer.writerow(elem)

# read_file = json.load(json_file)
# data_list = []
# for item in read_file:
#     data_list = [{'name': item['employeeName'], 'cost': item['directCost']} for item in read_file]
#
# output_csv =f"output_files/1chr/{json_name.replace('input_files/1chr/', '').replace('.json', '')}.csv"
#
# with open(output_csv, 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=['name', 'cost'])
#     writer.writeheader()
#     if data_list:
#         for elem in data_list:
#             writer.writerow(elem)

