from bs4 import BeautifulSoup


# Method signature: find_next_siblings(name, attrs, string, limit, **kwargs)
# Method signature: find_next_sibling(name, attrs, string, **kwargs)


soup = BeautifulSoup(open('main.html'), 'lxml')
first_link = soup.a

last_link = first_link.find_next_sibling(id='link3')

print(last_link)

print()

print(first_link.find_next_siblings('a'))

print()

first_story_paragraph = soup.find("p", "story")
print(first_story_paragraph.find_next_sibling("p"))
