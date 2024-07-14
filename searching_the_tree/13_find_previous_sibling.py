from bs4 import BeautifulSoup


# Method signature: find_previous_siblings(name, attrs, string, limit, **kwargs)

# Method signature: find_previous_sibling(name, attrs, string, **kwargs)

soup = BeautifulSoup(open('./main.html'), 'lxml')

last_link = soup.find("a", id="link3")
last_link
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

last_link.find_previous_siblings("a")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

first_story_paragraph = soup.find("p", "story")
first_story_paragraph.find_previous_sibling("p")
# <p class="title"><b>The Dormouse's story</b></p>
