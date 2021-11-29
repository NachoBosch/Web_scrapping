from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://es.wikipedia.org/wiki/Revoluci%C3%B3n_de_Mayo').text
soup = BeautifulSoup(html_text,'lxml')
text = soup.find_all('p')
print(text)
# for index,job in enumerate(jobs):
# 	company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
# 	skills = job.find('span', class_='srp-skills').text.replace(' ','')
# 	published_date= job.find('span',class_='sim-posted').text.replace(' ','')
# 	more_info = job.header.h2.a['href']
# 	if unfamiliar_skill not in skills:
# 		with open (f'Posts/{index}.txt','w') as f:
# 			f.write(f'Company Name: {company_name}\n')
# 			f.write(f'Required Skills: {skills}\n')
# 			f.write(f'Published Dates: {published_date}\n')
# 			f.write(f'More Info: {more_info}')