import re
import requests
import xml.etree.ElementTree as ET

# Download XML file from URL
url = "https://apteka.magnit.ru/api/feeds/newbigfeed.xml"
response = requests.get(url)
xml_string = response.text

# xml_string = 'Эрадикация Helicobacter pylor у больных с язвенной болезнью желудка или двенадцатиперстной кишки (всегда в комбинации с другими препаратами) '
# # Remove ASCII codes in hexadecimal notation
# # xml_string = re.sub('\xa0', '', xml_string)
# xml_string = xml_string.encode('ascii', errors='ignore')


# def remove_hex(string):
#     result = ""
#     for char in string:
#         if not(char.isdigit() or char.isalpha() or char in [' ', '\t', '\n', '\r', '?', '<', '>', '.', ',']):
#         # if not (char = is_hex):
#             # if the character is not alphanumeric or a whitespace character, remove it
#             continue
#         else:
#             result += char
#     return result
#
# xml_string = remove_hex(xml_string)

xml_string = re.sub('[\x00-\x09\xa0-\xa9\xac-\xae\x0b\x0c]', '', xml_string)

# Write the modified XML string to a file
with open('output_files/newbigfeed.xml', 'w') as f:
    f.write(xml_string)

# # Parse the modified XML string back into an ElementTree object for further processing if needed
# root = ET.fromstring(xml_string)

print("all done!")

print("check commit")
