from bs4 import BeautifulSoup

### .contents and .children

# A tag’s children are available in a list called .contents:

file = open('story.html')
soup = BeautifulSoup(file, 'lxml')
head_tag = soup.head
print(head_tag)

print(head_tag.contents)

title_tag = head_tag.contents[0]
print(title_tag)
print(title_tag.contents)

for child in title_tag.children:  # children is a generator contents is a list
	print(child)
