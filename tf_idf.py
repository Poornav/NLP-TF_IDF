def tfidf(exactMatch,queryList,DocUnigram,listOfFiles):
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
    
