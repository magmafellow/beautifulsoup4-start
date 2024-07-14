from bs4 import BeautifulSoup
import re


def not_lacie(href):
    return href and not re.compile("lacie").search(href)

soup = BeautifulSoup(open('main.html'), 'html.parser')

print(soup.find_all(href=not_lacie))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


# id is any keyword arg. So it is treated as attribute of a descendant(found) tag
soup.find_all(id=['link1', re.compile('3$')]) # [<a class=”sister” href=”http://example.com/elsie” id=”link1”>Elsie</a>, # <a class=”sister” href=”http://example.com/tillie” id=”link3”>Tillie</a>]


data_soup = BeautifulSoup('<div data-foo="value">foo!</div>', 'html.parser')
# data_soup.find_all(data-foo="value")  # this is no acceptable argument name use this instead
r = data_soup.find_all(attrs={'data-foo': 'value'})
print(r)
