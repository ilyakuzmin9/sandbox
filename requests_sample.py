import requests

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQzVwd1IA3lPiqth6B2MNT4OZ_7KG9dUtwWKNuJeqGFe5xHAKkxuOtqS3OxmL3hWTYe8DvJEimU7O2d/pub?gid=695844956&single=true&output=csv"
resp = requests.get(url)
print(resp.text)
