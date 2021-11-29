from bs4 import BeautifulSoup
import requests
import time

#print('Put some skill that you are not familiar with')
#unfamiliar_skill = input('>')
#print(f"Filtering out {unfamiliar_skill}")
#html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
#print(html_text)#200 is a conventional number for the requests donde sucefully
#soup = BeautifulSoup(html_text,'lxml')
#content = soup.find('li', class_='clearfix job-bx wht-shd-bx')
#print(content)
#company_name = soup.find('h3',class_='joblist-comp-name').text.replace(' ','')
#skills = soup.find('span', class_='srp-skills').text.replace(' ','')
#published_date= soup.find('span',class_='sim-posted').text
#print(skills)
#print(company_name)
# print(f'''
# 	Company Name: {company_name}
# 	Required Skills: {skills}
# 	''')
#print(f"Published Date:{published_date}")

##.----------The Same but in a For Loop through some jobs--------.##
print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f"Filtering out {unfamiliar_skill}")

def find_jobs():
	html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
	soup = BeautifulSoup(html_text,'lxml')
	jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
	for index,job in enumerate(jobs):
		company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
		skills = job.find('span', class_='srp-skills').text.replace(' ','')
		published_date= job.find('span',class_='sim-posted').text.replace(' ','')
		more_info = job.header.h2.a['href']
		if unfamiliar_skill not in skills:
			with open (f'Posts/{index}.txt','w') as f:
				f.write(f'Company Name: {company_name}\n')
				f.write(f'Required Skills: {skills}\n')
				f.write(f'Published Dates: {published_date}\n')
				f.write(f'More Info: {more_info}')

if __name__ == '__main__':
	while True:
		find_jobs()
		time_wait = 10
		print(f'Waiting {time_wait} minutes')
		time.sleep(time_wait*60)