from bs4 import BeautifulSoup
import requests
from perToJson import perToJson
import asyncio

def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)

    return wrapped

@background
def func_call(url, name, count):
    perToJson(url, name)
    print(count)
    return 0


url = 'https://www.astro.com/wiki/astro-databank/index.php?title=Special:AllPages&from=AA+Tool&namespace=112'
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
ul = soup.find('ul', class_='mw-allpages-chunk')
a = ul.find_all('a')

#href contain all links on the page of individual name
href = [a[i].get('href') for i in range(len(a))]
print(href)

count = 0
for link in href:
    url = 'https://www.astro.com'+link
    l_split = link.split('/')
    name = l_split[-1]
    count = count+1
    try:
        func_call(url, name, count)
    except:
        print(f'Error in url: {url}')