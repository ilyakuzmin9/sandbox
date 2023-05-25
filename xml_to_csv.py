import csv
import xml.etree.ElementTree as ET


def extract_values_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    values = []

    for offer in root.iter('offer'):
        try:
            offer_id = offer.get('id')
        except AttributeError:
            offer_id = 'none'
        try:
            offer_available = offer.get('available')
        except AttributeError:
            offer_available = 'none'
        try:
            offer_url = offer.find('url').text
        except AttributeError:
            offer_url = 'none'

        values.append((offer_id, offer_available, offer_url))

    return values


def save_to_csv(values, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['offer_id', 'offer_available', 'offer_url'])
        writer.writerows(values)

# Usage example
xml_file = 'input_files/test_dir/yandex_market_feed_full_all_regions_krasnodar.yml'
csv_file = 'output_files/test_dir/yandex_market_feed_full_all_regions_krasnodar.csv'

extracted_values = extract_values_from_xml(xml_file)
save_to_csv(extracted_values, csv_file)


print("all done!")
