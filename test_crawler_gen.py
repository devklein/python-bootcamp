import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# define a class with variables for the single elements
class CrawledArticle():
    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image

# define a class to fetch the page, parse the content, assign it to the variables and put it in a list        
class ArticleFetcher():
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"
        

        while url != " ":
            print(url)
            time.sleep(1)
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")
            
            for card in doc.select(".card"):
                emoji = card.select_one(".emoji").text
                content = card.select_one(".card-text").text
                title = card.select(".card-title span")[1].text
                image = urljoin(url, card.select_one("img").attrs["src"])

                yield CrawledArticle(title, emoji, content, image)
                

            button = doc.select_one(".navigation .btn")

            # as long as there's a next page button, pass the url in the loop
            if button:
                next_page = urljoin(url, button.attrs["href"])
                url = next_page
            else:
                url = " "    

         
        return articles


fetcher = ArticleFetcher()

counter = 0

for element in fetcher.fetch(): 
    if counter == 9:
        break

    counter += 1
    print(element.emoji + " " + element.title)
