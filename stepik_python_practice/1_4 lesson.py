from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

# В файле находится одна таблица.
# Просуммируйте все числа в ней.
resp = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html') # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
data = soup.find_all('td')
number = [int(d.text) for d in data]
print(sum(number))

# В файле находится одна таблица.
# Просуммируйте все числа в ней.
# Теперь мы добавили разных тегов для изменения стиля отображения.
# Для доступа к ячейкам используйте возможности BeautifulSoup.
resp1 = urlopen('https://stepik.org/media/attachments/lesson/209723/4.html') # скачиваем файл
html = resp1.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
data = soup.find_all('td')
number = [int(d.text) for d in data]
print(*number)
print(sum(number))

resp2 = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html') # скачиваем файл
html = resp2.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
data = soup.find_all('td')
number = [int(d.text) for d in data]
print(sum(number))
