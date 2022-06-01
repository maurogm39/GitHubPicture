import requests
from bs4 import BeautifulSoup as bs 
import webbrowser


github_user= input("Enter the GitHub username: ")

url = "https://github.com/" + github_user

r = requests.get(url)

soup = bs(r.content, "html.parser")

profile_image=soup.find("img", {"alt":"Avatar"})["src"]

webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application//chrome.exe"))
webbrowser.get('chrome').open_new(profile_image)
