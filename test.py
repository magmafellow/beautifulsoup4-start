from bs4 import BeautifulSoup


soup = BeautifulSoup(open('index.html'), 'lxml')

prolog = soup.find(id='pre')
print(prolog)

link = soup.find(href='https://google.com')
print(link)
