from bs4 import BeautifulSoup


# css_soup = BeautifulSoup('<p class="body"></p>', 'html.parser')
# print(css_soup.p['class'])

# css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
# print(css_soup.p['class'])


# rel_soup = BeautifulSoup('<p>Back to the <a rel="index first">homepage</a></p>', 'html.parser')
# rel_soup.a['rel']
# # ['index', 'first']
# rel_soup.a['rel'] = ['index', 'contents']
# print(rel_soup.p)
# # <p>Back to the <a rel="index contents">homepage</a></p>


# id is not a multi-valued attribute so it is treated as a string
# id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
# print(id_soup.p['id'])


# turn off multi-valued attributes
# no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser', multi_valued_attributes=None)
# print(no_list_soup.p['class'])
# 'body strikeout'


# id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
# print(id_soup.p['id'])
# 'my id'
# print(id_soup.p.get_attribute_list('id'))
# ["my id"]


# If you parse a document as XML, there are no multi-valued attributes:
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
print(xml_soup.p['class'])
# 'body strikeout'
