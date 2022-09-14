import requests
from bs4 import BeautifulSoup


url = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(url)
# print(response.status_code) #check the status of request
# print(response.text) #check results of request
# print(response.request.headers) #check the headers of request
# print(response.headers)
# print(response)
page = BeautifulSoup(response.text, "html.parser")
print(page.title.string)
# print(page.find_all('h3'))
link_section = page.find('h3', attrs={'id': 'chars'})
section = []
for element in link_section.next_elements:
    if element.name == 'h3':
        break
    section.append(element.string or '')
result = ''.join(section)
print(result)
    