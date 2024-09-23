#Realizar web scraping na página de avaliações da Amazon para extrair o nome do livro e o nome do autor a partir da seguinte URL:
#https://www.amazon.com.br/Web-Scraping-Python-Ryan-Mitchell/product-reviews/1491985577/ref=cm_cr_unknown?ie=UTF8&reviewerType=all_reviews&pageNumber=1&filterByStar=five_star
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('https://www.amazon.com.br/Web-Scraping-Python-Ryan-Mitchell/product-reviews/1491985577/ref=cm_cr_unknown?ie=UTF8&reviewerType=all_reviews&pageNumber=1&filterByStar=five_star')

div_info = driver.find_element(By.CLASS_NAME, 'product-info')

print(div_info.text)
