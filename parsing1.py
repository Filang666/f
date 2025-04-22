from bs4 import BeautifulSoup
import requests
from move import move
from shutil import rmtree
from os import mkdir
import ssl


def pars():
	ssl._create_default_https_context = ssl._create_unverified_context
	rmtree("pdf")
	mkdir("pdf")
	days = ["Вторник", "Суббота", "Пятница", "Четверг", "Среда", "Понедельник"]
	url = 'https://sortavala-school1.ru/life/schedule1/#'
	page = requests.get(url, verify=False)
	soup = BeautifulSoup(page.text, "html.parser")
	print(page.status_code)
	for b, a in enumerate(soup.findAll('a', class_='mr-1 sf-link sf-link-theme sf-link-dashed')):
		name = a['href']
		fileName = days[b] + ".pdf"
		with open(fileName, "wb") as file:
			response = requests.get('https://sortavala-school1.ru' + name)	
			file.write(response.content)
		move('pdf', fileName)
		

