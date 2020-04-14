import xmltodict

fin = open('map2.osm', 'r', encoding='utf8')
text = fin.read()
fin.close()

names = []   # список с названиями машазинов, котрые встречаются
stations = 0
dct = xmltodict.parse(text)
for node in dct['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        flag = False
        name = 'noname'
        if isinstance(tags, list): # првкерить является ли тэг списком
            for tag in tags:
                if '@k' in tag and tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                    stations += 1
                    flag = True
                if '@k' in tag and tag['@k'] == 'name':
                    name = tag['@v']

        elif isinstance(tags,dict):
                if tags['@v']=='fuel':
                    stations += 1
                    flag = True

        if flag:
            names.append(name)

print(stations)
print(*names)
