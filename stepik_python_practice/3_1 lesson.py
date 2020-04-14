import xmltodict

dct=xmltodict.parse("""<?xml version="1.0" ?>
<person>
  <name>john</name>
  <age>20</age>
</person>""")
# {u'person': {u'age': u'20', u'name': u'john'}}

print(dct['person'])

fin = open('map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()


parsedxml = xmltodict.parse(xml)
print(parsedxml['osm']['node'][100]['@id'])
