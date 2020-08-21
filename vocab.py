import csv
import json
from konlpy.tag import Hannanum
hannanum = Hannanum()

file = open('economic_news.csv','r',encoding='utf-8')
rdr = csv.reader(file)
contentsList = []
for line in rdr:
    contentsList.append(line[1])
file.close()

vocab = []
for contents in contentsList:
    temp = hannanum.morphs(contents)
    for elem in temp:
        if(not(elem in vocab)):
            vocab.append(elem)

file_data = {}
i=0
for elem in vocab:
    file_data[str(i)] = elem
    i += 1

with open('vocab.json','w',encoding='UTF-8') as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
