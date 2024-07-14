from bs4 import BeautifulSoup


soup = BeautifulSoup(open('main.html'), 'lxml')

## By default, mytag.find_all() will examine all the descendants of mytag: its children, its children’s children, and so on.
##   To consider only direct children,you can pass in recursive=False. See the difference here:

print(soup.html.find_all('title', recursive=False))

print('-' * 8)

print(soup.html.find_all('title'))
