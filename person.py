# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.astro.com/astro-databank/1943_Frankford_Junction_derailment'
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

table  = soup.find('table', class_="infobox toccolours")
td = table.find_all('td')
print(len(td))

data = {} # persons data
data['Name'] = td[2].text
data['Gender'] = td[3].text[9:-1]
if td[-13].small == None:
    data['Born on'] =  td[-13].get_text(strip = True)
    data['Born Time'] = None
else:
    at = td[-13].text.find('at')
    data['Born on'] = td[-13].text[:at]
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
print(data)

tag_itr = soup.h2.parent.children

count = -1
for tag in tag_itr:
    print(f'cname : {tag.name}')
    if tag.name == 'h2':
        count = count+1
        header = tag.text
        data[header] = []
        print(header)
        index = 0
        continue
    if count == -1:
        pass
    else:
        try:
            print(f'ctext : {tag.get_text()}')
            tag_txt = tag.get_text(strip=True).replace(u'\xa0', ' ')
            data[header].append(tag_txt)
            index =index+1
        except:
            print('Error in extracting Data')

wiki = soup.find('a', class_ = 'extiw')
if wiki:
    data['wiki'] = wiki.get('href')
    data['Biography'] = data['Biography'][0:-1]
else:
    data['wiki'] = None
print(data)
js_data = json.dumps(data ,indent=2)
with open('data.json','w') as fp:
    json.dump(data, fp, indent=2)
    # js = json.load(fp)
    # js = [json.loads(line) for line in fp]

    # print(js)
