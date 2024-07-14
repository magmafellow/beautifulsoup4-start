from bs4 import BeautifulSoup
from bs4 import NavigableString
import re


def has_class_but_no_id(tag):
  if tag.has_attr('class') and not tag.has_attr('id'):
    return True
  return False

soup = BeautifulSoup(open('main.html'), 'lxml')

# for tag in soup.find_all(has_class_but_no_id):
#   print(tag)


def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))

for tag in soup.find_all(surrounded_by_strings):
    print(tag.name)
