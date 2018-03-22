# CS410-Location-Recommendation
**For detailed documentation, please refer to the [wiki page](https://github.com/YuchenLiDaniel/CS410-Location-Recommendation/wiki)**

CS 410 course project working on location recommendation from Twitter data

1. Files

data/
- contains the data files (if a data file is too large to be included in GitHub, it is usually shared in Google Drive via email).

learner/
- contains a draft for pre-processing

read_pickle.py
- contains a helper function that reads a pickle file 
- use its function read_pickle() to read the pickle file containing the tokenized Twitter dataset (tweets1100000_tokenized.pickle). An example usage is provided in its main function.
- check how to import helper function in Python and how to set the file path of the input file before using this function

tokenize.py
- tokenizes Twitter data using nltk.tokenize.TweetTokenizer
- convert each data (originally a string) to a Tweet object, defined in this file as class Tweet
