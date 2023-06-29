import requests
import os
import csv
import json
from time import sleep


def get_geo_points(a_token, a_address):
    req = requests.get(f"https://geocode-maps.yandex.ru/1.x/?format=json&apikey={a_token}&geocode={a_address}")
    sleep(0.5)
    json_data = json.loads(req.text)
    point = json_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    long, lat = point.split()
    return long, lat


if __name__ == '__main__':
    # address = 'Красноуфимск Ачитская 1'
    token = os.environ.get('TOKEN')
    addresses_list = []
    with open('input_files/addresses/addresses.csv', newline='') as input_file:
        reader = csv.DictReader(input_file, delimiter='\t')
        for line in reader:
            addresses_list.append(line)

    for item in addresses_list:
        result = get_geo_points(token, item['modify_address'])
        item['long'] = result[0]
        item['lat'] = result[1]

    with open('output_files/addresses/output_addresses.csv', 'w', newline='') as output_file:
        fieldnames = list(addresses_list[0].keys())
        writer = csv.DictWriter(output_file, delimiter='\t', fieldnames=fieldnames)
        writer.writeheader()
        for elem in addresses_list:
            writer.writerow(elem)

    print('done')




