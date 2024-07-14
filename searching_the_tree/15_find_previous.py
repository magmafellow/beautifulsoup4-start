from bs4 import BeautifulSoup


# Method signature: find_all_previous(name, attrs, string, limit, **kwargs)

# Method signature: find_previous(name, attrs, string, **kwargs)

soup = BeautifulSoup(open('main.html'), 'lxml')

first_link = soup.a
first_link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

first_link.find_all_previous("p")
# [<p class="story">Once upon a time there were three little sisters; ...</p>,
#  <p class="title"><b>The Dormouse's story</b></p>]

first_link.find_previous("title")
# <title>The Dormouse's story</title>
