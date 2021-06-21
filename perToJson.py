# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import time

# url = 'https://www.astro.com/astro-databank/Accidents:_West_Fertilizer_Company_explosion_(Waco'
def perToJson(url, fn):
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

    table  = soup.find('table', class_="infobox toccolours")
    td = table.find_all('td')
    # print(len(td))

    data = {} # persons data
    data['Name'] = td[2].text
    data['Gender'] = td[3].text[9:-1]
    if td[-13].small == None:
        data['Born on'] =  td[-13].get_text(strip = True)
        data['Born Time'] = None
    else:
        at = td[-13].text.find('at')
        data['Born on'] = td[-13].text[:at].strip()
        data['Born Time'] = td[-13].small.text[2:-1].strip()
    data['Place'] = td[-11].text.replace(td[-11].small.text, '').strip()
    data['latitude'] = td[-11].small.get_text(strip =  True)
    data['TimeZone'] = td[-9].text[:-1]
    data['Data Source'] = td[-6].text
    data['Rodden Rating'] = td[-4].text[14:-1]
    data['Collector'] = td[-3].text[11:-1]
    data['Astrology data'] = td[-1].text[:-1]
    if len(td) == 20: 
        data['Birthname'] = td[5].text[:-1]

    tag_itr = soup.h2.parent.children

    count = -1
    for tag in tag_itr:
        # print(f'cname : {tag.name}')
        if tag.name == 'h2':
            count = count+1
            header = tag.text
            data[header] = []
            # print(header)
            index = 0
            continue
        if count == -1:
            pass
        else:
            try:
                # print(f'ctext : {tag.get_text()}')
                tag_txt = tag.get_text(strip=True).replace(u'\xa0', ' ')
                data[header].append(tag_txt)
                index =index+1
            except:
                # print('Error in extracting Data')
                pass

    wiki = soup.find('a', class_ = 'extiw')
    if wiki:
        data['wiki'] = wiki.get('href')
        data['Biography'] = data['Biography'][0:-1]
    else:
        data['wiki'] = None
    # print(data)
    js_data = json.dumps(data ,indent=2)
    file_name = 'data/'+fn+'.json'
    with open(file_name,'w') as fp:
        json.dump(data, fp, indent=2)
    return

if __name__ == "__main__":
    url = 'https://www.astro.com/astro-databank/Ackley,_Gardner'
    fn= 'data'
    perToJson(url, fn)

