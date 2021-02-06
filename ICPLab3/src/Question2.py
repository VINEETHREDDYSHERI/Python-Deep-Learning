# Importing the packages
import requests
from bs4 import BeautifulSoup

html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")  # Getting the content of the site
bsObj = BeautifulSoup(html.content, "html.parser")  # Parsing the html data
print("The Title of the page is: ", bsObj.title.string)

linksData = bsObj.find_all("a")  # Getting all the <a> links details
outPutFile = open("WikiPageLinks.txt", "w")  # Opening the file in write mode
for link in linksData:
    if link.get('href') is not None:
        outPutFile.write(str(link.get('href')) + "\n")  # Writing the urls into the file.

print()
print("Writing the links information to the file is completed")
