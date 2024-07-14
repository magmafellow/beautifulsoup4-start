from bs4 import BeautifulSoup


soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
tag.string
# 'Extremely bold'
print(type(tag.string))
# <class 'bs4.element.NavigableString'>

unicode_string = str(tag.string)
print(unicode_string)


# You can’t edit a string in place, but you can replace one string with another, using replace_with():
tag.string.replace_with('Updated bold text')
print(tag)



















