from bs4 import BeautifulSoup


### .parent

# soup = BeautifulSoup(open('../story.html'), 'html.parser')
# title_tag = soup.title

# print(title_tag)  # title
# print(title_tag.parent)  # head

# print(title_tag.string.parent)  # returning to title

# print(soup.html.parent == soup)

# print(soup.parent is None)


### .parents

soup = BeautifulSoup(open('../story.html'), 'html.parser')

link = soup.a
print(link)

for parent in link.parents:
  print(parent.name)
