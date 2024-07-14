from bs4 import BeautifulSoup


### .next_element and .previous_element¶

soup = BeautifulSoup(open('../story.html'), 'html.parser')

last_a_tag = soup.find('a', id='link3')
# print(last_a_tag.next_sibling)

# print(last_a_tag.next_element)


# print(last_a_tag.previous_element)


### .next_elements and .previous_elements¶

for element in last_a_tag.next_elements:
  print(element)
