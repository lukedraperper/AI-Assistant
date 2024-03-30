from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.request import Request

def GetTable():
    my_url = "https://www.premierleague.com/tables"
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    top = page_soup.find("span", {"class":"long"}).text
    tottenham = page_soup.find("tr", {"data-filtered-table-row-name":"Tottenham Hotspur"})
    tottenhamplace = tottenham.span.text
    if top == "Tottenham Hotspur":
        sayMessage = "Currently, " + top + " are at the top of the Premier League Table."
    else:
        sayMessage = "Currently, " + top + " are at the top of the Premier League Table whilst Tottenham are at Position", tottenhamplace
    return sayMessage
def NextFixture():
    my_url = "https://www.tottenhamhotspur.com/fixtures/men/"
    req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
    uClient = uReq(req)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    dayname = page_soup.find("div",{"class":"FixtureHero__kickoff"})

    return dayname