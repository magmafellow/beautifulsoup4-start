from bs4 import BeautifulSoup
import re


soup = BeautifulSoup(open('main.html'), 'lxml')

# print(soup.find_all('a', class_='sister'))


# print(soup.find_all(class_=re.compile("itl")))
# [<p class="title"><b>The Dormouse's story</b></p>]

print()

def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6

# print(soup.find_all(class_=has_six_characters))


##

css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
# print(css_soup.find_all("p", class_="strikeout"))
# [<p class="body strikeout"></p>]

# print(css_soup.find_all("p", class_="body"))
# [<p class="body strikeout"></p>]



# a trick in studio
# print(soup.find_all('a', attrs={'class': 'sister'}))

# must have method
print(css_soup.select('p.body.strikeout'))
