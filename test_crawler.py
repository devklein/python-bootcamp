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
        articles = []

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

                crawled = CrawledArticle(title, emoji, content, image)
                articles.append(crawled)

            button = doc.select_one(".navigation .btn")

            # as long as there's a next page button, pass the url in the loop
            if button:
                next_page = urljoin(url, button.attrs["href"])
                url = next_page
            else:
                url = " "    

         
        return articles


fetcher = ArticleFetcher()

for element in fetcher.fetch(): 
    print(element.emoji + " " + element.title)