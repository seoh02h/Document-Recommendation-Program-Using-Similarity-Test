from recommendationProgram import *
titleList, contentsList = readCsv()
frequency = readTxt()
currpage = 1
lastpage = 66
showPage(currpage,currPageTitle(currpage,titleList))

while(1):
    inputData = input("input Title / 'next' / 'word' / 'exit' : ")
    if(inputData == "next") :
        if(currpage == lastpage):
            currpage = 1
        else:
            currpage +=1
            showPage(currpage,currPageTitle(currpage,titleList))
    elif(inputData=="word"):
        keyword = input("word input : ")
        result = searchWord(keyword, frequency,titleList)
        showTitle(result)
    elif(inputData == "exit"):
        break
    else:
        for tit in titleList:
            if (inputData == tit):
                idx = titleList.index(tit)
                print(contentsList[titleList.index(tit)])
                print("\nSimilar Documents")
                similarityResult = similarityTest(idx,contentsList,titleList)
                showTitle(similarityResult)

                print("\nTop Ranking Word")
                RankingWordResult = topRankingWord(idx, frequency)
                for i in range(5):
                    print(str(i+1)+". "+RankingWordResult[i][0])
                break