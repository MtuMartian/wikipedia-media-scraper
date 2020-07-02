from bs4 import BeautifulSoup
import requests

url = input("Enter wiki page to scrape: ")

soup = BeautifulSoup(requests.get(url).text)

links = soup.findAll("a", {"class": "galleryfilename"})

for link in links:
    url = 'https://commons.wikipedia.org' + link.attrs["href"]
    soup = BeautifulSoup(requests.get(url).text)

    mediaDiv = soup.find("div", {"class": "fullMedia"})

    url = mediaDiv.a.attrs["href"]
    fileName = mediaDiv.a.attrs["title"].replace(" ", "_")
    res = requests.get(url)
    open(fileName, "wb").write(res.content)
