from urllib.request import urlopen
html = urlopen("http://ru.wikipedia.org/wiki/Python").read().decode("utf-8")
print(type(html))
s = str(html)  # Необязательно
print(html.count("C++"))
print(html.count("Python"))
state = 0
ans = []
for c in s:
    if c == "<":
        state = 1
    if c == ">":
        state = 0
    elif state == 0:
        ans.append(c)
print(ans)
s = ''.join(ans)
print(s.count("C++"))

