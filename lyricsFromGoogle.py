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



headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }



searchPage = requests.get(searchSong, headers=headers_Get)
html = BeautifulSoup(searchPage.text,'html.parser')
lyrics=html.find_all("span", jsname="YS01Ge")
if lyrics==[]:
	print('Couldn\'t get lyrics')
else:
	for i in lyrics:
		print(i.get_text())




b = datetime.datetime.now()
delta=b-a
print('Time taken in millisecond: ',delta.total_seconds() * 1000)
