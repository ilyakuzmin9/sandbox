import time

import requests
from create_random_mac_list import write_list_to_csv, generate_mac_list
from hex_to_bytes import mac_list_to_md5
from rewriting_csv_from_directories import process_csv_files
import os
import json
import time


# response_json = '{"segment":{"id":29618136,"type":"uploading","status":"uploaded","has_guests":false,"guest_quantity":0,"can_create_dependent":false,"has_derivatives":false,"hashed":false,"item_quantity":9885,"guest":false}}'
# y = json.loads(response_json)
# id = y['segment']



input_dir = 'input_files/mac_hashes/'
output_dir = 'output_files/mac_hashes/'

# process_csv_files(input_dir, output_dir)

# mac_list = generate_mac_list(100)
# hashed_mac_list = mac_list_to_md5(mac_list)
# output_file = 'output_files/random_mac_list.csv'
# write_list_to_csv(output_file, hashed_mac_list)

def make_request_for_upload_csv_file(a_url, a_file_path, a_headers):
    """
    Uploads a CSV file to the specified URL using the provided headers.
    Returns True if the response status code is 200, otherwise returns False.
    """
    files = [('file', (a_file_path, open(a_file_path, 'rb'),'text/csv'))]
    response = requests.post(a_url, headers=a_headers, files=files)
    if response.status_code == 200:
        print('File uploaded successfully.')
        print(f"{response.status_code} - {response.text}")
        response_json = json.loads(response.text)
        segment_id = {'id': response_json['segment']['id'], 'name': os.path.basename(a_file_path)}
        return segment_id
    else:
        print(f'Error uploading file: {response.status_code} - {response.text}')
        return False

def make_request_for_save_segment(s_segment):
    url = f"https://api-audience.yandex.ru/v1/management/segment/{s_segment['id']}/confirm?checkSize=true"
    payload = json.dumps({
        "segment": {
            "id": int(s_segment['id']),
            "content_type": "mac",
            "hashed": True,
            "name": s_segment['name']
        }
    })
    headers = {
        'Authorization': 'OAuth AQAAAAAZpTe7AAQ2zclBUPsmG0ipnc7fHPM5gsY',
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    print(f"{response.status_code} - {response.text}")
    time.sleep(15)
    return response_json

def save_segments(a_segment_id_list):
    json_data_list = []
    for segment in a_segment_id_list:
        json_data = make_request_for_save_segment(segment)
        json_data_list.append(json_data)

    return json_data_list


def make_request_for_update_segment(a_segments_list, a_input_dir, a_headers):
    """
    Uploads a CSV file to the specified URL using the provided headers.
    Returns True if the response status code is 200, otherwise returns False.
    """
    response_list = []
    for item in a_segments_list:
        file_path = f"{a_input_dir}/{item['file']}"

        files = [('file', (file_path, open(file_path, 'rb'), 'text/csv'))]
        response = requests.post(f"https://api-audience.yandex.ru/v1/management/segment/{item['segment']}/modify_data?modification_type=addition", headers=a_headers, files=files)
        if response.status_code == 200:
            print('File uploaded successfully.')
            print(f"{response.status_code} - {response.text}")
            response_json = json.loads(response.text)
            response_list.append(response_json)
            # segment_id = {'id': response_json['segment']['id'], 'name': os.path.basename(file_path)}
        else:
            print(f'Error uploading file: {response.status_code} - {response.text}')
            response_json = json.loads(response.text)
            response_list.append(response_json)
    return response_list


inp_dir = 'input_files/update_segments'
segment_list = [{'segment': '29619093', 'file': 'Gallery_Angstrem_20230322_20230331_VLG.csv'},
                {'segment': '29619092', 'file': 'Gallery_Angstrem_20230322_20230331_VOR.csv'},
                {'segment': '29619091', 'file': 'Gallery_Angstrem_20230322_20230331_MOS.csv'},
                {'segment': '29619076', 'file': 'Gallery_Angstrem_20230322_20230331_SPB.csv'},
                {'segment': '29619075', 'file': 'Gallery_Angstrem_20230322_20230331_EKT.csv'},
                {'segment': '29619071', 'file': 'Gallery_Angstrem_20230322_20230331_NVS.csv'},
                {'segment': '29618989', 'file': 'Gallery_Angstrem_20230322_20230331_SOC.csv'},
                {'segment': '29618956', 'file': 'Gallery_Angstrem_20230322_20230331_KRA.csv'}]
request_headers = {'Authorization': 'OAuth AQAAAAAZpTe7AAQ2zclBUPsmG0ipnc7fHPM5gsY'}

resp = make_request_for_update_segment(segment_list, inp_dir, request_headers)



request_url = 'https://api-audience.yandex.ru/v1/management/segments/upload_csv_file?'
request_headers = {'Authorization': 'OAuth AQAAAAAZpTe7AAQ2zclBUPsmG0ipnc7fHPM5gsY'}

segment_id_list = []
for filename in os.listdir(output_dir):
    if filename.endswith('.csv'):
        segment_id = make_request_for_upload_csv_file(request_url, output_dir+filename, request_headers)
        segment_id_list.append(segment_id)
        time.sleep(1)



segments_json_data = save_segments(segment_id_list)

print(segments_json_data)


