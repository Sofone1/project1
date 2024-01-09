from bs4 import BeautifulSoup
import requests
import csv
import os

column_name = ['Entry Number', 'Name', 'Year', 'Genres', 'Movie Rating', 'Plot']
csvfile = open('movies.csv', 'w', newline='') 
csvwriter = csv.writer(csvfile)
csvwriter.writerow(column_name)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

website = requests.get("https://simkl.com/movies/best-movies/most-watched/", headers=headers).text
soup = BeautifulSoup(website, 'lxml')
movies = soup.find_all('table', class_= "SimklTVBestItems")
print(movies)
c = 0
for movie in movies:
    name = movie.find('td', class_= "SimklTVBestItemTitle").text
    name = name.strip()

    year = movie.find('span', class_= 'detailYearInfo').text
    genre = movie.find('td', class_= "SimklTVAboutGenre").text.split(', ')

    rating = movie.find('td', class_='SimklTVBestIcoScore').text

    info = movie.find('td', class_= 'SimklTVAboutDetailsText').text
    
    c+=1 # to check whether we are able to properly scrape the data for all 250 movies

    
    csvwriter.writerow([c, name, year, genre, rating, info]) 
    print(name)
    # print(year)
    # print(duration)
    # print(movieRated)
    # print(rating)
    # print(count) 
   
print(f"Done writing {c} entries to the csv file!")
csvfile.close()
