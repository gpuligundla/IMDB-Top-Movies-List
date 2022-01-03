import requests
import pandas
from bs4 import BeautifulSoup
import json

url = 'https://www.imdb.com/chart/top/'

response = requests.get(url).content

soup = BeautifulSoup(response,'html.parser')

title = soup.find_all('td', class_='titleColumn')

rating = soup.find_all('strong')

images = soup.find_all('img')

movie_name = []
movie_year =[]
movie_href =[]
movie_image = []
movie_rating = []

for t in title:
    imdb_title_num = t.a.get('href').split('/')[2]
    href = 'https://www.imdb.com/title/'+imdb_title_num
    movie_href.append(href)
    imdb_title = t.a.text
    movie_name.append(imdb_title)
    year = t.span.text
    movie_year.append(year)

for rate in rating:
    r = rate.text
    movie_rating.append(r)

for img in images:
    i = img.get('src')
    movie_image.append(i)

model = pandas.DataFrame({'title': movie_name, 'year': movie_year, 'rating': movie_rating, 'image': movie_image, 'href': movie_href})
model.to_json('movies_data.json', orient="records")