from bs4 import BeautifulSoup

### .descendants


# soup = BeautifulSoup(open('story.html'), 'html.parser')
# head_tag = soup.find('head')

# for child in head_tag.descendants:
# 	print(child)


# print(len(soup.contents))
# print(len(list(soup.descendants)))


### .string

## If a tag has only one child, and that child is a NavigableString, the child is made available as .string:

# soup = BeautifulSoup(open('story.html'), 'html.parser')
# title_tag = soup.title
# print(title_tag.get_text())
# print(title_tag.string)

## If a tag’s only child is another tag, and that tag has a .string, then the parent tag is considered to have the same .string as its child:
soup = BeautifulSoup(open('story.html'), 'html.parser')
title_tag = soup.title
head_tag = soup.head
print(head_tag.string)  # the same
print(title_tag.string) # the same


print(soup.html.string)  # None









