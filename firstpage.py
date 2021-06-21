from bs4 import BeautifulSoup
import requests
url = "https://www.astro.com/astro-databank/Main_Page"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
# print(soup.title.text)
span = soup.findAll('span',class_ = "plainlinks")
# href = span.a.get('href')
href = [span[i].a.get('href') for i in range(len(span))]

print(href[0])


