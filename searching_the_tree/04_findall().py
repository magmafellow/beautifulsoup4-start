from bs4 import BeautifulSoup


### find_all()
# find_all(name, attrs, recursive, string, limit, **kwargs)

with open('main.html', 'r') as file:
	soup = BeautifulSoup(file, 'lxml')

	# print(soup.find_all('title'))

	print(soup.find_all('p', {'be': 'yellow'}))
	print(soup.find_all('p', 'title'))

	# print(soup.find_all('a'))

	# print(soup.find_all(id='link2'))

	import re
	# print(soup.find(string=re.compile('sisters')))

