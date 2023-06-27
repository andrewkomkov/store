import requests
from bs4 import BeautifulSoup

# Загрузка страницы
url = 'http://auto.tgvpn.tk/?target=map'
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Извлечение HTML-кода страницы
    html = response.text
    
    # Создание объекта BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    # Нахождение всех элементов <a> на странице
    links = soup.find_all('a')
    
    # Обход каждой найденной ссылки
    for link in links:
        # Получение URL ссылки
        href = link.get('href')
        print(href)  # Вывод URL ссылки или можно выполнить другие действия
else:
    print('Ошибка при загрузке страницы:', response.status_code)
