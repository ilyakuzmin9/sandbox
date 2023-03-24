import requests
from create_random_mac_list import write_list_to_csv, generate_mac_list
from hex_to_bytes import mac_list_to_md5
from rewriting_csv_from_directories import process_csv_files
import os
import json

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
    segment_id_list = []
    files = [('file', (a_file_path, open(a_file_path, 'rb'),'text/csv'))]
    response = requests.post(a_url, headers=a_headers, files=files)
    if response.status_code == 200:
        print('File uploaded successfully.')
        response_json = json.loads(response.text)
        segment_id = response_json['segment']['id']
        segment_id_list.append({'id': segment_id, 'name': os.path.basename(a_file_path)})
        return segment_id_list
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
    return response_json

def save_segments(a_segment_id_list):
    json_data_list = []
    for segment in a_segment_id_list:
        json_data = make_request_for_save_segment(segment)
        json_data_list.append(json_data)

    return json_data_list


request_url = 'https://api-audience.yandex.ru/v1/management/segments/upload_csv_file?'
request_headrs = {'Authorization': 'OAuth AQAAAAAZpTe7AAQ2zclBUPsmG0ipnc7fHPM5gsY'}

for filename in os.listdir(output_dir):
    if filename.endswith('.csv'):
        segment_id_list = make_request_for_upload_csv_file(request_url, output_dir+filename, request_headrs)


segments_json_data = save_segments(segment_id_list)

print(segments_json_data)


