from bs4 import BeautifulSoup


### .strings and stripped_strings¶

soup = BeautifulSoup(open('story.html'), 'html.parser')

for string in soup.strings:
	print(string)

# Newlines and spaces that separate tags are also strings.
#   You can remove extra whitespace by using the .stripped_strings generator instead:

for string in soup.stripped_strings:
	print(string)
