import re
from urllib.request import urlopen
html = urlopen("file:///C:/Users/E277460/Downloads/2.html").read().decode("utf-8")
s = str(html)  # not necessary ?
result = re.findall("<code>(.*?)</code>", s) # list of strings placed between <code> and </code>
d = {}
for i in result:
    if i in d:
        d[i] += 1
    else:
        d[i] = 0
for keys, val in sorted(d.items(), key=lambda x: -x[1]): # value from high to low
    print(keys, val)


# https://www.dataquest.io/blog/web-scraping-tutorial-python/
