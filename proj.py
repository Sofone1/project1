from bs4 import BeautifulSoup
import requests
import csv
import os

column_name = ['Name', 'Date', 'Rating', 'Anime type', 'Duration/Episodes']
csvfile = open('anime_data.csv', 'w', newline='') 
csvwriter = csv.writer(csvfile)
csvwriter.writerow(column_name)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

website = requests.get("https://anilist.co/search/anime?genres=Detective", headers=headers).text
soup = BeautifulSoup(website, 'lxml')
animes = soup.find_all('div', class_= "media-card")
print(animes)
c = 0
for anime in animes:
    name = anime.find('a', class_= "title").text.split('. ')[1:]
    name = "{}".format(*name)

    date = anime.find('div', class_= 'date')

    rating = anime.find('span', class_= 'percentage')

    animeData = anime.find_all('div', class_= 'typings')
    
    type = animeData[0].text
    episodes = animeData[2].text

    c+=1

    csvwriter.writerow([c, name, date, rating, type, episodes])

print(f"Done writing {c} entries to the csv file!")
csvfile.close()