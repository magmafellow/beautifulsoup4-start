from bs4 import BeautifulSoup


soup = BeautifulSoup(open('main.html'), 'html.parser')

for i in soup.find_all(['a', 'b']):
  print(i)
