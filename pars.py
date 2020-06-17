import requests
from bs4 import BeautifulSoup
from re import search

phone = input('phone: ')
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/78.0.3904.108 Chrome/78.0.3904.108 Safari/537.36'}
resp = requests.get('https://mirror.bullshit.agency/search_by_phone/' + phone,headers=headers)
soup = BeautifulSoup(resp.text,'html.parser')

for i in soup.find('div',class_='row row-eq-height').find('div',class_='col-sm-8').find_all('a'):
	text = i.find_all('span','text-muted')
	link = i.get('href')

	if 'avito.ru' not in link:
		resp_link = requests.get('https://mirror.bullshit.agency' + link)
		soup_link = BeautifulSoup(resp_link.text,'html.parser')
		link = soup_link.find('a',class_='btn btn-default').get('href')

	print('Subject: ' + i.find('h4','media-heading').get_text())
	print('Text: ' + text[0].get_text())
	print('Date: ' + text[1].get_text())
	print('Link: ' + link)
	print('\n')
