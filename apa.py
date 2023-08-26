import requests as re

url = input("Pega la url de la página que quieres citar: \n")
response = re.get('https://www.youtube.com/watch?v=osJ-DkpiEPU')
html = response.text

print(html)
