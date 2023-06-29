import csv
import xml.etree.ElementTree as ET
import requests




def csv_to_xml(a_url, xml_path):

    response = requests.get(a_url)
    content = response.content.decode('utf-8')  # Decode the content from bytes to string
    csv_data = csv.reader(content.splitlines())



    headers = next(csv_data)

    root = ET.Element('data')
    for row in csv_data:
        item = ET.SubElement(root, 'item')
        for idx, value in enumerate(row):
            field_name = headers[idx]
            field = ET.SubElement(item, field_name)
            field.text = value

    xml_tree = ET.ElementTree(root)
    xml_tree.write(xml_path, encoding='utf-8', xml_declaration=True)


# Example usage:
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQB1tYtNXbiE27krGWZF_9Ae5l_wvtyLYyBYj2vi4DSkPWAOJ8MDlBi7_m2-On6weGKeTbY0lv3ICnd/pub?gid=1992701458&single=true&output=csv"
xml_file_path = 'output_files/xml_feeds/output.xml'
csv_to_xml(url, xml_file_path)
