from bs4 import BeautifulSoup
import requests
from perToJson import perToJson
import time

link_count = 0
data_ectracted = 0
next_link_count = 4 # check next page link is there or only previous page
url = 'https://www.astro.com/astro-databank/Special:Allpages?from=A'
# url= 'https://www.astro.com/wiki/astro-databank/index.php?title=Special:AllPages&from=Claverie%2C+Pierre'
while next_link_count>2:
    get_link_data = False
    while get_link_data==False:
        try:
            req = requests.get(url, timeout = 5)
            get_link_data = True
        except:
            get_link_data = False
            time.sleep(2)
            print('stuck')
    soup = BeautifulSoup(req.text, "html.parser")
    ul = soup.find('ul', class_='mw-allpages-chunk')
    a_of_person = ul.find_all('a')


    #href contain all links on the page of individual name
    href = [a_of_person[i].get('href') for i in range(len(a_of_person))]
    link_count = link_count+len(href)
    # print(link_count)
    a_of_next_page = soup.find_all('a', title = 'Special:AllPages')
    # print(len(a_of_next_page))
    next_link_count = len(a_of_next_page)
    url = "https://www.astro.com"+a_of_next_page[-1].get('href')
    print(url)
    # time.sleep(100)
    # print(href[265])
        
    for link in href:
        person_url = 'https://www.astro.com'+link
        l_split = link.split('/')
        name = l_split[-1]
        try:
            perToJson(person_url, name)
            data_ectracted = data_ectracted + 1
        except:
            print(f'Error with url: {person_url}')
    print(f'Number of data extracted: {data_ectracted}')
print(f'total links: {link_count}')
print(f'Final of data extracted: {data_ectracted}')