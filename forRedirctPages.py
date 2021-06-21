from bs4 import BeautifulSoup
import requests
from perToJson import perToJson
import time

def forRedirectPages(url):
    get_link_data = False
    while get_link_data==False:
        try:
            req = requests.get(url)
            get_link_data = True
        except:
            get_link_data = False
            time.sleep(2)
            print('stuck in person url')
    soup = BeautifulSoup(req.text, "html.parser")
    ul = soup.find('ul', class_ = 'redirectText')
    if ul:
        person_url = "https://www.astro.com" + ul.a.get('href')
        l_split = person_url.split('/')
        name = l_split[-1]
        try:
            perToJson(person_url, name)
            return True
        except:
            print(f'Tried redirected page But no result: {person_url}')
            return False
    else:
        print(f'There is no redirect and No person data: {url}')
        return False

if __name__ == "__main__":
    # url = 'https://www.astro.com/astro-databank/Twins_Green,_Eva_%2B_Joy'
    # name = 'AAAAA'
    # forRedirectPages(url, name)
    with open('console.txt', 'r') as fp:
        lines= fp.readlines()
        print(len(lines))
    
    url_count =0
    data_extracted_count = 0 
    for line in lines:
        if line.find("with url")>0:
            url = line.replace("Error with url:",'').strip()
            result = forRedirectPages(url)
            if result:
                data_extracted_count = data_extracted_count + 1
            # print(f'url: {url}')
            url_count = url_count+1
    print(f'url count: {url_count}')
    print(f'data extracted count: {data_extracted_count}')
