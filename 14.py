#14 Faça web scraping para obter a lista dos 100 livros mais baixados no dia anterior (Top 100 EBooks Yesterday) a partir da URL https://www.gutenberg.org/browse/scores/top.
# A execução do script deve retornar uma lista dos 100 livros mais baixados ontem, com o seguinte formato: {Título - Downloads qtd \n Link : url}

import urllib.request

from bs4 import BeautifulSoup

url = 'https://www.gutenberg.org/browse/scores/top'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.6'}


request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
    
soup = BeautifulSoup(html, 'html.parser')
        
table_100_ebooks = soup.find('ol')

for row in table_100_ebooks.find_all('a'):
    link = row.get('href')
    index_end_title = row.text.find('(')
    title = row.text[:index_end_title]
    qtd_downloads = row.text[index_end_title+1: -1]
    print(f'{title} - Downloads: {qtd_downloads} \n Link: https://gutenberg.org{link}')
    
    