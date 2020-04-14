 # https://stepik.org/lesson/245678/step/1?unit=217895

import xmltodict

fin = open('map1.osm', 'r', encoding='utf8')
text = fin.read()
fin.close()

shops = 0
dct = xmltodict.parse(text)
for node in dct['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        if isinstance(tags, list): # првкерить является ли тэг списком
            for tag in tags:
                print(tag)
                if '@k' in tag and tag['@k'] == 'shop':
                    shops += 1
print(shops)
