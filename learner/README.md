This folder contains two files, search.py and create_Inverted_Index.py. The first one searches and returns the document frequency (i.e., the number of tweets)
where a keyword exists), total frequency (i.e., the total number of times that the keyword exists) and a dictionary that maps the ID of document to the number
of times that the keyword occurs in that tweet. The second one constructs the inverted index that enables the searching.

The inverted index is stored in twenty .pickle files due to the large size. search.py searches each .pickle files and add the result together.
