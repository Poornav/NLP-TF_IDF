Given a query string q and a corpus of documents, retrieve the top k documents that are the closest match


Dataset:

A list of cricket commentary units. A single unit of cricket commentary is the commentary for 1 ball and this constitutes 1 document.

Pre Processing (using NLTK api) :

a. Tokenization (Sentence and Word levels)

b. Case conversions

c. Stop-word removal

d. Lemmatization or stemming


Requirements of the project :

a. If the query contains the term 'boundary' it should match both FOUR and SIX.

b. The term couple may correspond to 2 runs and should be treated equivalent.

c. The numeric value of FOUR (or any such word that corresponds to a number) should match the numeric value 4 also and likewise for other
words that represent numbers.

4. Pre-compute the term frequency scores for the documents. This also serves as the index of different tokens in the document.

5. You are required to handle exclamation marks and question marks that may be found in the query

6. You are required to compute TFIDF scoring for the normalized query string against each normalized document in the corpus

7. Return the top 10 documents ordered as per the rank, where the first document in the list is the document that has the top rank

8. You should handle conditions like: If the query contains any word that is not found in the document, you should leave that word out while computing the score. Implement this algorithm without add 1 smoothing. (If none of the documents in the whole corpus contains any word in the query string the score

should be zero for that query for each document.)

9. We require that the implementation specified above returns documents that match the query where the query terms are considered as logical OR.