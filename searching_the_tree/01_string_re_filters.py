from bs4 import BeautifulSoup
import re


soup = BeautifulSoup(open('main.html'), 'lxml')

# the simplest filter is a string. This will find by tag name against a given string
# print(soup.find_all('b'))

# another filter is regular expression filter
# for tag in soup.find_all(re.compile('^b')):
#   print(tag.name)

# This code finds all the tags whose names contain the letter ‘t’:
# for tag in soup.find_all(re.compile("t")):
#     print(tag.name)
# html
# title

# matches every tag
for tag in soup.find_all(True):
  print(tag.name)
