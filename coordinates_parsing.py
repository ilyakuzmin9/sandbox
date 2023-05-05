import xml.etree.ElementTree as et
import os
import csv


def get_file_from_directory(a_input_dir) -> list:
    path_dict_list = []
    for filename in os.listdir(a_input_dir):
        if filename.endswith('.kml'):
            # Set the input file paths
            input_file_path = os.path.join(a_input_dir, filename)
            input_file_name = filename
            path_dict = {'path': input_file_path, 'name': filename}
            path_dict_list.append(path_dict)

    return path_dict_list


def set_file_to_directory(a_output_dir, a_file_name, a_list_dicts):
    os.makedirs(a_output_dir, exist_ok=True)
    output_file = os.path.join(a_output_dir, a_file_name.replace('.kml', '.csv'))
    # Open the output file in write mode
    with open(output_file, 'w', newline='', ) as outfile:
        writer = csv.DictWriter(outfile, fieldnames=a_list_dicts[0].keys())
        writer.writeheader()
        for row in a_list_dicts:
            writer.writerow(row)


def kml_parse(file_path) -> list:
    tree = et.parse(file_path)
    # get the root element
    root = tree.getroot()
    # loop through the Placemark elements
    result_list_dict = []
    for placemark in root.findall('.//{*}Placemark'):
        # get the description value
        description = placemark.find('.//{*}description').text
        # extract the values from the description
        values = description.split('|')
        name = values[2]
        # time = values[3]
        # address = values[4]
        # get the coordinates value
        coordinates = placemark.find('.//{*}coordinates').text.strip()
        # split the coordinates into pairs
        pairs = coordinates.split(' ')
        # print the pairs
        coordinates_str = ', '.join([f'[{s}]' for s in pairs])

        result_dict = {'name': name, 'points': coordinates_str}

        result_list_dict.append(result_dict)

    return result_list_dict


input_dir = 'input_files/coordinates/'
output_dir = 'output_files/coordinates/'
files_path_list = get_file_from_directory(input_dir)
for item in files_path_list:
    result = kml_parse(item['path'])
    set_file_to_directory(output_dir, item['name'], result)





