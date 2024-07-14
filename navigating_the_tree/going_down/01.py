from bs4 import BeautifulSoup


with open('story.html') as file:
	soup = BeautifulSoup(file, 'lxml')
	head = soup.find('head')
	print(head)  # head tag
	print(soup.head)  # an equivalent

	print(soup.title)

	# you can zoom in
	print(soup.body.b)

	## find() (and its convenience equivalent) gives you only the first tag by that name:
	print(soup.a)  # first a

	# if you need all a tags use .find_all('a')
	print(soup.find_all('a'))
	