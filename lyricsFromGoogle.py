import requests
from bs4 import BeautifulSoup, UnicodeDammit
import datetime
searchSong='https://www.google.com/search?q='
s=input('Enter the song to find its lyrics: ')

#calculating time taken in searching lyrics
a = datetime.datetime.now()
for i in s:
	if i==' ':
		searchSong+='+'	
	else:
		searchSong+=i
searchSong+='+lyrics'
searchPage = requests.get(searchSong)

html = BeautifulSoup(searchPage.text, "html.parser")

try:
	playMusicTag=html.find("a", {"class":"fl"})
	playMusicLink=playMusicTag.get('href')
	lyricsPage=requests.get(playMusicLink)
	playMusicHTML = BeautifulSoup(lyricsPage.text, "html.parser")
	for i in playMusicHTML.find_all("br"):
		i.replace_with('\n')
	lyricsDiv=playMusicHTML.find("div", {"class":"content-container lyrics"})
	lyricsPara=lyricsDiv.findChildren("p")
	for i in lyricsPara:
		print(i.text)
except:
	print("Couldn't get lyrics")
b = datetime.datetime.now()
delta=b-a
print('Time taken in millisecond: ',delta.total_seconds() * 1000)
