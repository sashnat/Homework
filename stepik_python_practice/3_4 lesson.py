import xmltodict
import urllib.request

urllib.request.urlretrieve(r'https://stepik.org/media/attachments/lesson/245681/map2.osm', 'map2.osm')


fin = open('map2.osm', 'r', encoding='utf8')
text = fin.read()
fin.close()

names = []   # список с названиями машазинов, котрые встречаются
stations = 0
stats = 0
stations1 = 0
stats1 = 0

dct = xmltodict.parse(text)
#print(dct['osm']['node'])
#print(dct['osm'])
#print(dct['osm']['way'])
for node in dct['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        flag = False
        name = 'noname'
        if isinstance(tags, list): # првкерить является ли тэг списком
            #print(tags)
            for tag in tags:
                if '@k' in tag and tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                    #print(tags)
                    stations += 1
                    flag = True
                if '@k' in tag and tag['@k'] == 'name':
                    name = tag['@v']

        elif isinstance(tags,dict):
                if tags['@v']=='fuel':
                    stats += 1
                    flag = True

        if flag:
            names.append(name)

for node in dct['osm']['way']:
    if 'tag' in node:
        tags = node['tag']
        flag = False
        name = 'noname'
        if isinstance(tags, list): # првкерить является ли тэг списком
            #print(tags)
            for tag in tags:
                if '@k' in tag and tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                    #print(tags)
                    stations1 += 1
                    flag = True
                if '@k' in tag and tag['@k'] == 'name':
                    name = tag['@v']

        elif isinstance(tags,dict):
                if tags['@v']=='fuel':
                    stats1 += 1
                    flag = True

        if flag:
            names.append(name)
sum = stations + stats + stations1 + stats1
print(sum, stations, stats, stations1, stats1 )
print(*names, len(names))
print(len(names))

'''
parsedxml = xmltodict.parse(xml)
for some in parsedxml['osm']:
  if isinstance(parsedxml['osm'][some], list):
    for some_with_tag in parsedxml['osm'][some]: 
      if 'tag' in some_with_tag:
'''
