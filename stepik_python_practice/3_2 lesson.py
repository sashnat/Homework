import xmltodict

fin = open('map1 (1).osm', 'r', encoding='utf8')
text = fin.read()
fin.close()
sum1 = 0
sum2 = 0
dct = xmltodict.parse(text)
for node in dct['osm']['node']:
    if 'tag' in node:
        sum1 += 1
    else:
        sum2 += 1
print (sum1, sum2)
