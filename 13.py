#13 Faça web scraping para extrair dados da tabela Downloaded Books da URL https://www.gutenberg.org/browse/scores/top, que contém informações sobre o número de livros baixados nas últimas datas.
# Armazene os dados extraídos (data e número de downloads) em um dicionário ou estrutura apropriada para impressão posterior.

import urllib.request

from bs4 import BeautifulSoup

url = 'https://www.gutenberg.org/browse/scores/top'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.6'}


request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
    
soup = BeautifulSoup(html, 'html.parser')
        
table_downloaded_books = soup.find('table')

downloaded_books = {}

for row in table_downloaded_books.find_all('tr'):
    keys = row.find_all('th')
    values = row.find_all('td')
    if keys and values:
        downloaded_books[keys[0].text] = values[0].text

print(downloaded_books)