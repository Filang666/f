from bs4 import BeautifulSoup
import requests
import shutil
import os

url = 'https://sortavala-school1.ru/life/schedule1/#'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
print(page.status_code)


for a in soup.findAll('a', class_='mr-1 sf-link sf-link-theme sf-link-dashed'):
	name = a['href']
	fileName = name[19:len(name)]
	with open(fileName, "wb") as file:
        	response = requests.get('https://sortavala-school1.ru' + name)	
        	file.write(response.content)
	shutil.copy(os.path.join('.', fileName), os.path.join('result'))
	os.remove(os.path.join('.', fileName))
