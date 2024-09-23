import re
import urllib.request
from bs4 import BeautifulSoup


url = 'http://quotes.toscrape.com/'

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

quotes = soup.find_all('div', class_='quote')

padrao_limpeza = re.compile(r'[^\w\s]')

palavra_chave = "beterraba"

filtered_quotes = {}

for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    if palavra_chave in text:
        filtered_quotes[author] = padrao_limpeza.sub('', text)

if filtered_quotes:
    for author, quote in filtered_quotes.items():
        print(f'Citação (filtrada por palavra-chava {palavra_chave}): {quote} \n Autor: {author}')
else:
    print(f'Não foram encontradas citações com a palavra: {palavra_chave}')    

