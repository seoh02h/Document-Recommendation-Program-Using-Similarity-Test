import csv
from konlpy.tag import Okt
from collections import Counter

file = open('economic_news.csv','r',encoding='utf-8')
rdr = csv.reader(file)
contentsList = []
for line in rdr:
    contentsList.append(line[1])
file.close()

okt = Okt()
wordsList = []

for contents in contentsList:
    wordsList.append(okt.nouns(contents))

frequency = []
for words in wordsList:
    frequency.append(Counter(words))


file = open('forsearchword.txt', 'w', encoding='utf-8')
file.write(str(frequency))
file.close()

