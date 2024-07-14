from bs4 import BeautifulSoup


# Method signature: find(name, attrs, recursive, string, **kwargs)
## The find_all() method scans the entire document looking for results, but sometimes you only want to find one result. If you know a document has only one <body> tag, it’s a waste of time to scan the entire document looking for more. Rather than passing in limit=1 every time you call find_all, you can use the find() method. These two lines of code are nearly equivalent:

soup = BeautifulSoup(open('main.html', 'r'), 'lxml')

print(soup.find_all('title', limit=1))
# [<title>The Dormouse's story</title>]

print(soup.find('title'))
# <title>The Dormouse's story</title>


###

soup.head.title
# <title>The Dormouse's story</title>

soup.find("head").find("title")
# <title>The Dormouse's story</title>
