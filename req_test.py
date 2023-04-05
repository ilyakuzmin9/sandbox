import requests

url = "https://neofeeds.iprospect.app/api/client/Globus/project/smartbanners/feed/yandex-combined?authorizationKey=mE68MEPs59Pz5Ce"
response = requests.get(url)
xml_string = response.text
with open('output_files/test_feed.xml', 'w') as f:
    f.write(xml_string)

print("all done!")