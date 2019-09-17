import os

def readStopwords(language):
    '''
    returns stopwords as strings
    '''    
    filename = "stopwordsEN.txt"
    path = os.path.join("app/static/", filename)
    file = open(path, 'r')
    return file.read().splitlines()  # splitlines is used to remove newlines