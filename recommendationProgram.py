import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from konlpy.tag import Okt
from collections import Counter

def readCsv():
    file = open('economic_news.csv','r',encoding='utf-8')
    rdr = csv.reader(file)
    titleList = []
    contentsList = []
    for line in rdr:
        titleList.append(line[0])
        contentsList.append(line[1])
    file.close()
    return titleList, contentsList

def readTxt():
    file = open('forsearchword.txt','r', encoding='utf-8')
    data = file.read()
    frequency = eval(data)
    return frequency

def currPageTitle(pageNum, titleList):
    titles = []
    for i in range(pageNum * 15 - 15, pageNum * 15):
        titles.append(titleList[i])
    return titles

def showPage(pageNum,titles):
    titleNum = pageNum*15-14
    for title in titles:
        print(str(titleNum) + " : " + title)
        titleNum +=1

def searchWord(keyword,frequency,titleList):
    freqDic = {}
    for i in range(1005):
        freqDic[i] = frequency[i][keyword]
    freqView = [(freq, key) for key, freq in freqDic.items()]
    freqView.sort(reverse=True)
    n = 1
    result = []
    for freq, key in freqView:
        if (freq > 5):
            result.append(titleList[key])
    return result

def similarityTest(idx, contentsList,titleList):
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(contentsList)
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    result = []
    for score in sim_scores:
        result.append(titleList[score[0]])
    return result

def showTitle(result):
    n = 1
    for title in result:
        print(str(n)+". "+title)
        n +=1

def topRankingWord(idx,frequency):
    okt = Okt()
    result = []
    result = frequency[idx].most_common(5)
    return result







