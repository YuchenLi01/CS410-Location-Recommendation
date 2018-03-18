This folder contains two files, search.py and create_Inverted_Index.py. The first one searches and returns the document frequency (i.e., the number of tweets)
where a keyword exists), total frequency (i.e., the total number of times that the keyword exists) and a dictionary that maps the ID of document to the number
of times that the keyword occurs in that tweet. The second one constructs the inverted index that enables the searching.

The inverted index is stored in the .pickle file uploaded to 410 google drive (in the same directory as the notes and proposal). 

Update: 1. I find that self.text is the most appropriate test used for search. Self.word_tokens contain too much stop words. I also tried some other tokenize tools but still found that self.text is best. 
        2. I feel that we need to store the top 10000 frequent (in document frequency) terms in the inverted index instead of 5000, since there are a total of 500000+ different terms in the tweets. 
        3. If the search.py is stored in directory /xxx, then the tweets1100000_partial_0_.pickle should be located in  xxx/data/tweets1100000_partial_0_.pickle
