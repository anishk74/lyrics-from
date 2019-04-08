import requests
from bs4 import BeautifulSoup, UnicodeDammit	
import re
from unidecode import unidecode
import datetime
def stripper(song, artist):
	"""
	Generate the url path given the song and artist to format the Genius URL with.
	Strips the song and artist of special characters and unresolved text such as 'feat.' or text within braces.
	Then concatenates both with hyphens replacing the blank spaces.
	Eg.
	>>>stripper('Paradise City', 'Guns n’ Roses')
	Guns-n-Roses-Paradise-City
	Which then formats the url to https://genius.com/Guns-n-Roses-Paradise-City-lyrics
	:param song: currently playing song
	:param artist: song artist
	:return: formatted url path
	"""
	song = re.sub(r'\([^)]*\)', '', song).strip()  # remove braces and included text
	song = re.sub('- .*', '', song).strip()  # remove text after '- '
	song_data = artist + '-' + song
	# Remove special characters and spaces
	url_data = song_data.replace('&', 'and')
	# re.sub(r"[^a-zA-Z0-9]+", '', url_data) does work of below lines
	# url_data = url_data.replace('/', ' ')  potentially replace / with space to support more songs, needs testing
	for ch in [',', "'", '!', '.', '’', '"', '+', '?', 'Σ', '#', '/', '$', 'Ø', 'ø', '%', ':', '|']:
		if ch in url_data:
			url_data = url_data.replace(ch, '')
	url_data = ' '.join(url_data.split())  # remove multiple spaces to one space
	url_data = url_data.replace(' ', '-')  # hyphenate the words together
	url_data = unidecode(url_data)  # remove accents and other diacritics
	return url_data


song = input("Enter the name of song: ")
artist=input("Enter the artist name: ")
#calculating time taken in searching lyrics
a = datetime.datetime.now()
url_data = stripper(song, artist)  # generate url path using stripper()
url = 'https://genius.com/{}-lyrics'.format(url_data)  # format the url with the url path
page = requests.get(url)
if page.status_code != 200:
	url_data = requests.get('https://aadibajpai.pythonanywhere.com/stripper', data={'song': song, 'artist': artist}).text
	url = 'https://genius.com/{}-lyrics'.format(url_data)
	page = requests.get(url)
html = BeautifulSoup(page.text, "html.parser")
# TODO: Add error handling
lyrics_path = html.find("div", class_="lyrics")  # finding div on Genius containing the lyrics
if lyrics_path is None:
	
	lyrics = 'Couldn\'t get lyrics for {song} by {artist}.\n'.format(song=song, artist=artist)
	
else:
	lyrics = UnicodeDammit(lyrics_path.get_text().strip()).unicode_markup
print(lyrics)
b = datetime.datetime.now()
delta=b-a
print('Time taken in millisecond: ',delta.total_seconds() * 1000)


