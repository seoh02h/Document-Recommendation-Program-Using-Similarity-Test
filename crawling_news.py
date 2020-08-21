import requests
from bs4 import BeautifulSoup
import csv

def createCsv(title,contents):
    file = open('economic_news.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([title, contents])
    file.close()

def appendCsv(title,contents):
    file = open('economic_news.csv','a',newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([title,contents])
    file.close()

def getArticle(link,flag):
    URL = link
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    title = soup.find("h1",{"id":"article_title"}).text.strip()
    contents = soup.find("div",{"id":"article_body"})

    for br in contents.select('br'):
        span=soup.new_tag('span')
        span.string = '\n'
        br.insert_after(span)
        br.unwrap()
    contents = contents.text.strip()

    if(flag==1):
        createCsv(title,contents)
    else:
        appendCsv(title,contents)

def extractLinks(URL):
        result = requests.get(URL)
        result.encoding = None
        soup = BeautifulSoup(result.text, "html.parser")
        articleList = soup.select("#content > div.list_basic.list_sectionhome > ul > li")
        linkList = []
        for li in articleList:
            linkList.append(li.find('h2').find('a')["href"])
        return linkList


lastPage = 68
URL = "https://news.joins.com/money"
for pageNum in range(1, lastPage):
    currentURL = f"{URL}?page={pageNum}"
    linkList = extractLinks(currentURL)
    for i in range(len(linkList)):
        getArticle(linkList[i], pageNum+i)
