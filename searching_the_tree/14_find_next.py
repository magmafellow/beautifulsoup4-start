from bs4 import BeautifulSoup


# Method signature: find_all_next(name, attrs, string, limit, **kwargs)

# Method signature: find_next(name, attrs, string, **kwargs)

soup = BeautifulSoup(open('main.html'), 'lxml')

first_link = soup.a
first_link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

first_link.find_all_next(string=True)
# ['Elsie', ',\n', 'Lacie', ' and\n', 'Tillie',
#  ';\nand they lived at the bottom of a well.', '\n', '...', '\n']

first_link.find_next("p")
# <p class="story">...</p>
