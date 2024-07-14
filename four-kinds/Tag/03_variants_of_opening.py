from bs4 import BeautifulSoup


with open('index.html') as fp:
  soup = BeautifulSoup(fp, 'lxml')
  print(soup.get_text())
  

# alternative option is just a string
soup = BeautifulSoup('<html>a web page</html>', 'lxml')
