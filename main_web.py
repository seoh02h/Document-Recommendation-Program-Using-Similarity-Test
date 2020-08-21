from flask import Flask, render_template, request
from recommendationProgram import *

titleList, contentsList = readCsv()
frequency = readTxt()

lastpage = 66

app = Flask("main_web")

@app.route("/")
def home():
    currpage = 1
    showtitle = currPageTitle(currpage,titleList)
    return render_template("index.html", showtitle = showtitle, currpage=currpage)

@app.route("/next")
def next():
    currpage = int(request.args.get('page'))
    showtitle = currPageTitle(currpage, titleList)
    return render_template("next.html", showtitle=showtitle, currpage=currpage)


@app.route("/documents")
def documents():
    idx = int(request.args.get('title'))
    simimlarityResult = similarityTest(idx, contentsList, titleList)
    RankingWordResult = topRankingWord(idx, frequency)
    return render_template("documents.html", title = titleList[idx], contents = contentsList[idx], sim = simimlarityResult, words = RankingWordResult)

@app.route("/word")
def word():
    keyword = request.args.get('word')
    result = searchWord(keyword, frequency, titleList)
    return render_template("word.html",keyword=keyword,result=result, n =len(result))

app.run()