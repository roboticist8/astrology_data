from bs4 import BeautifulSoup
import requests
from perToJson import perToJson

url = 'https://www.astro.com/wiki/astro-databank/index.php?title=Special:AllPages&from=1943+Frankford+Junction+derailment'
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
ul = soup.find('ul', class_='mw-allpages-chunk')
a = ul.find_all('a')

#href contain all links on the page of individual name
href = [a[i].get('href') for i in range(len(a))]
print(href)
for link in href:
    url = 'https://www.astro.com'+link
    l_split = link.split('/')
    name = l_split[-1]
    try:
        perToJson(url, name)
    except:
        print(f'Error in url: {url}')