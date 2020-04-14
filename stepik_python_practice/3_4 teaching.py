# вызов консоли в браузере ctrl+shift+I

import xmltodict
import urllib.request

urllib.request.urlretrieve('https://www.openstreetmap.org/api/0.6/map?bbox=37.5882%2C55.752%2C37.6136%2C55.7574', 'map2.osm')

fin = open('map2.osm', 'r', encoding='utf8')
text = fin.read()
fin.close()

names = []   # список с названиями машазинов, котрые встречаются
shops = 0
dct = xmltodict.parse(text)
for node in dct['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        flag = False
        name = 'noname'
        if isinstance(tags, list): # првкерить является ли тэг списком
            for tag in tags:
                if '@k' in tag and tag['@k'] == 'shop' and tag['@v'] == 'supermarket':
                    shops += 1
                    flag = True
                if '@k' in tag and tag['@k'] == 'name':
                    name = tag['@v']
        if flag:
            names.append(name)

print(shops)
print(*names)

