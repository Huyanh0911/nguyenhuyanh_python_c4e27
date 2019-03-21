from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode('utf-8')
soup = BeautifulSoup(html_content,"html.parser")
section = soup.find("section","section chart-grid")
li_list=section.div.ul.find_all("li")
for li in li_list:
    h3=li.h3.a
    h4=li.h4.a
    namesong=h3.string
    artists=h4.string
    # print(namesong)
    # print(artists)
    # print("*"*50)
new_list=[]
for li in li_list:
    h3=li.h3.a
    h4=li.h4.a
    namesong=h3.string
    artists=h4.string
    news = ( {
        "namesong":namesong,
        "artists":artists})
    new_list.append(news)
# pyexcel.save_as(records=new_list, dest_file_name="songandartists.xlsx")
from youtube_dl import YoutubeDL
for news in new_list:
    name = news["namesong"]
    art = news["artists"]
    options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1, 
    'format': 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download([name])
