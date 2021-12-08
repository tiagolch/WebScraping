import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.remessaonline.com.br/cotacao/cotacao-dolar')
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, 'html.parser')

find = soup.find_all("div", attrs={"class" : "style__Text-sc-15flwue-2 cSuXFv"})

for finded in find:
    valor = finded.text
    print(f'A cotação do Dolar hoje esta a R${valor}')





