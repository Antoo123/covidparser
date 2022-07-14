import requests 
from bs4 import BeautifulSoup
link='https://www.meteoservice.ru/archive/avtovo/'

year=2019
month=0
day=0
for y in range(3):
	year+=1
	day=0
	year=0
	for m in range(12):
		day=0
		month+=1
		for d in range(30):
			day+=1
			link='https://www.meteoservice.ru/archive/avtovo/'+str(year)+'/0'+str(month)+'/'+'0'+str(day)
			response=requests.get(link).text
			soup=BeautifulSoup(response,'lxml')
			# inf=soup.find('h1',class_='text-center smedium-text-left')
			# print(inf)
			print(link)