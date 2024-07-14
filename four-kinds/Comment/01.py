from bs4 import BeautifulSoup


markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
# print(type(comment))
# <class 'bs4.element.Comment'>
# print(comment)
# Hey, buddy. Want to buy a used parser?

## The Comment object is just a special type of NavigableString:

print(soup.b.prettify())
