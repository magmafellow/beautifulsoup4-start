from bs4 import BeautifulSoup


soup = BeautifulSoup(open('main.html'), 'lxml')


# tag name
# print(soup.css.select('title'))

# print(soup.css.select('p:nth-of-type(3)'))

# tag by id
# print(soup.css.select('#link1'))
# print(soup.select('#link2'))

# nested tags
# print(soup.css.select('body a'))
# print(soup.css.select('html head title'))

# tags directly within other tags
# print(soup.css.select('p > a'))
# print(soup.select('head > title'))
# print(soup.select('p > a:nth-of-type(2)'))
# print(soup.css.select('body > a'))

# find all matching next siblings of tags
# print(soup.css.select('#link1 ~ .sister'))

# find the next sibling tag
# print(soup.css.select('#link1 + #link2'))  # results in tag
# print(soup.css.select('#link1 + #link3'))  # results in empty []

# find by css class
# print(soup.css.select('.sister'))
# print(soup.css.select('[class~=sister]'))

# any selector in list
# print(soup.css.select('#link1, #link3'))

# check an existence of an attribute
# print(soup.css.select('a[href]'))

# find tag by attribute value
# print(soup.css.select('a[href="http://example.com/elsie"]'))
# print(soup.css.select('a[href^="http://example.com/"]'))
# print(soup.css.select('a[href$="tillie"]'))
# print(soup.css.select('a[href*=".com/el"]'))

##### There’s also a method called select_one(), which finds only the first tag that matches a selector:

# print(soup.css.select_one('.sister'))

##### As a convenience, you can call select() and select_one() can directly on the BeautifulSoup or Tag object, omitting the .css property:

print(soup.select('a[href$="tillie"]'))
print(soup.select_one(".sister"))
