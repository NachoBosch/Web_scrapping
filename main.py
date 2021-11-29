from bs4 import BeautifulSoup

with open ('babyproduct.html','r') as f:
	content = f.read()
	#print(content)

	soup = BeautifulSoup(content,'lxml')
	#print(soup.prettify())

	#tags = soup.find('h1') #Just search for the first element that have the string
	#print(tags)
	tags = soup.find_all('div', class_='table') #This one show all the element with that string
	for tag in tags:
		#print(tag.text)
		#print(tag.th)
		print(tag.text.split())