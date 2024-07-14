from bs4 import BeautifulSoup

### .next_sibling and .previous_sibling¶

# sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>", 'html.parser')
# # print(sibling_soup.prettify())


# print(sibling_soup.b.next_sibling)

# print(sibling_soup.c.previous_sibling)


### .next_siblings and .previous_siblings¶
soup = BeautifulSoup(open('../story.html'), 'lxml')

for sibling in soup.a.next_siblings:
  print(repr(sibling))

print('-' * 8)

for sibling in soup.find(id='link3').previous_siblings:
  print(repr(sibling))
