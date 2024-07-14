from bs4 import BeautifulSoup


soup = BeautifulSoup(open('main.html'), 'lxml')

r = soup.find_all('a', limit=2)
print(r, len(r))
