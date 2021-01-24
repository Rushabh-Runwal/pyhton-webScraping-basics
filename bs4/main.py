from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
web_page = res.text

soup = BeautifulSoup(web_page, 'html.parser')

a = soup.find_all(name="h3",class_="title")[::-1]
m = []
for i in a:
    m.append(i.getText())
with open("movies.txt",'w',encoding="utf-8") as fl:
    [fl.write(f'{i}\n') for i in m]