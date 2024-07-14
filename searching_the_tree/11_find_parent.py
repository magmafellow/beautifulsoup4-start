from bs4 import BeautifulSoup


# Method signature: find_parents(name, attrs, string, limit, **kwargs)

# Method signature: find_parent(name, attrs, string, **kwargs)


# First let’s consider find_parents() and find_parent(). Remember that find_all() and find() work their way down the tree, looking at tag’s descendants. These methods do the opposite: they work their way up the tree, looking at a tag’s (or a string’s) parents. Let’s try them out, starting from a string buried deep in the “three daughters” document:

soup = BeautifulSoup(open('main.html', 'r'), 'lxml')

a_string = soup.find(string='Lacie')

print(a_string.find_parents('a'))

print(a_string.find_parent('p'))

print(a_string.find_parents("p", class_="title"))
