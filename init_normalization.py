from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import unicodedata
import re, math
exactMatch = False
word_lemmatizer = WordNetLemmatizer()
lookUpTable = {}
lookUpTable["boundary"] = ["4","four","six","6","boundary"]
lookUpTable["six"] = ["six","6"]
lookUpTable["6"] = ["six","6"]
lookUpTable["four"] = ["four","4"]
lookUpTable["4"] = ["four","4"]
lookUpTable["1"] = ["one","1","single"]
lookUpTable["couple"] = ["2","two","couple"]
lookUpTable["2"] = ["2","two","couple"]
lookUpTable["two"] = ["2","two","couple"]
lookUpTable["single"] = ["one","1","single"]
lookUpTable["one"] = ["one","1","single"]
lookUpTable["1"] = ["one","1","single"]
fp=open("Linear_full.txt",'w+')
listOfFiles=[]
stopWords = stopwords.words('english')
stopWords = list(set(stopWords) - set(["off","out","down","over","he","him","his","they","their"]))
m = 0
originalList = []
queryStr = raw_input("Enter a query ").lower()
if(queryStr[0] == "\"" and queryStr[len(queryStr) - 1] == "\""):
    exactMatch = True
queryStr = re.sub("[^A-Za-z0-9 ]+"," ",queryStr)

queryStr = queryStr.strip()
queryList = [str(word_lemmatizer.lemmatize(i)) for i in queryStr.split(" ") if(i not in stopWords) ]

N = 1500

for i in range(1,6):
    
    
    tempList = []
    tempStr = ""
    tempArr = []
    fs=open("Comments/50-overs/Linear/Linear-"+str(i)+".txt")
    tempStr = fs.read()
    tempList = tempStr.split("\", \"")
    tempStr = re.sub("[\[\]]+"," ",tempStr)
    originalList += tempStr.split("\", \"")

    
    
    
    listOfFiles.extend(tempList)
    #fp.write(r)
    #fs.close()
fp.write(str(listOfFiles))



for doc in range(len(listOfFiles)):
    tempList = []
    listOfFiles[doc] = listOfFiles[doc].lower() #.strip(",?!#@$%^&*[]*/\\;\"\'")
    listOfFiles[doc] = re.sub("[^A-Za-z0-9 ]+"," ",listOfFiles[doc])
    #   listOfFiles[doc] = listOfFiles[doc].replace(","," ")
    #tempList = [unicodedata.normalize('NFKD',word_lemmatizer.lemmatize(i)).encode('ascii','ignore') for i in listOfFiles[doc].split() if(i not in stopWords) ]
    tempList = [str(word_lemmatizer.lemmatize(i)) for i in listOfFiles[doc].split() if(i not in stopWords) ]
    listOfFiles[doc] = tempList
DocUnigram = []
countIDF = {}
for i in range(len(listOfFiles)):
    unigramWordCount = {}
    
    for j in range(len(listOfFiles[i])):
        word = listOfFiles[i][j]
        

        if unigramWordCount.has_key(word):
            unigramWordCount[word] += 1
        else:
            unigramWordCount[word] = 1

        if countIDF.has_key(word):
            if(unigramWordCount[word] == 1):
                countIDF[word] += 1
        else:
            countIDF[word] = 1

    DocUnigram.append(unigramWordCount)
rank = {}
if(exactMatch == False):
    for i in range(len(listOfFiles)):
        
        
        score = 0
        for word in queryList:
            found = False
            if(not DocUnigram[i].has_key(word)):
                if(lookUpTable.has_key(word)):
                    lookUpWord = lookUpTable[word]

                    for w in lookUpWord:
                        if(not DocUnigram[i].has_key(w)):
                            continue
                        else:
                            word = w
                            found = True
                            break
            else:
                found = True
            if(found == False):
                continue

            tf = float(DocUnigram[i][word])/len(DocUnigram[i])
            idf = math.log10(N/float(countIDF[word]))
            tfidf = tf * idf
            score += tfidf
        rank[i] = score
  
    
    
else:
    
    for i in range(len(listOfFiles)):
        
        found = True
        score = 0
        for word in queryList:

            if(not DocUnigram[i].has_key(word)):
                found = False
                break

            tf = float(DocUnigram[i][word])/len(DocUnigram[i])
            idf = math.log(N/float(countIDF[word]))
            tfidf = tf * idf
            score += tfidf
        if(found):
            rank[i] = score
        else:
            rank[i] = 0
    



rankKey = sorted(rank,key = rank.get)
rankValues = sorted(rank.values())
lenOfRank = len(rankKey)
printed = False
for i in range(10):
        if(rankValues[lenOfRank-i-1]== 0):
            continue
        printed = True
        print "Rank : ",(i+1)
        print "Score : ",rankValues[lenOfRank-i-1]
        print "Commentary : ",originalList[rankKey[lenOfRank-i-1]]
        
        print "-------------------------------------------------------------------------------------"

if(printed == False):
    print "Sorry.. Match not found for the query"

