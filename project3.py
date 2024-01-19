from bs4 import BeautifulSoup
import requests
import csv
import os
import re

column_name = ['Entry Number', 'Name', 'Type', 'Year', 'Status', 'Duration/Episodes', 'Genres']
csvfile = open('myanimes.csv', 'w', newline='', encoding= 'utf-8') 
csvwriter = csv.writer(csvfile)
csvwriter.writerow(column_name)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

website = requests.get("https://myanimelist.net/anime/genre/39/Detective", headers=headers).text
soup = BeautifulSoup(website, 'lxml')
animes = soup.find_all('div', class_= 'js-anime-category-producer seasonal-anime js-seasonal-anime js-anime-type-all js-anime-type-1')
print(animes)
c = 0
for anime in animes:
    name = anime.find('h2', class_= 'h2_anime_title').text
    name = name.strip()
    # print(name)

    info = anime.find('div', class_= 'info').text.split()
    type_year = info[0].split(',')
    type = re.sub(",", "", type_year[0])
    year_status = list(info[1])
    year1 = []
    x = 0
    while x < 4:
        year1.append(year_status[x])
        x+=1
        print(year1)
   
    year = ''.join(year1)
    status = []
    for i in year_status:
        if i not in year1:
            status.append(i)
    status = ''.join(status)
    episodes = info[2] + info[3] + ' ' + info[4] + info[5]
    # print(info)
    # print(type_year)
    # print(type)
    # print(year)
    # print(status)
    # print(episodes)

    genre = anime.find('div', class_= 'genres-inner js-genre-inner').text.split()
    c+=1

    # print(genre)
    # print(c)
    
    
    csvwriter.writerow([c, name, type, year, status, episodes, genre]) 
   
print(f"Done writing {c} entries to the csv file!")
csvfile.close()
