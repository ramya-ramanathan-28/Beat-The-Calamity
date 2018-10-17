from nltk.tokenize import word_tokenize
from nltk import ngrams
from folder import date

def get_ngrams(text, n ):
    n_grams = ngrams(word_tokenize(text), n)
    return [ ' '.join(grams) for grams in n_grams]



def fetch_items(hashtag):
    date.extract_tweet(hashtag)
    f = open('req.txt',encoding="utf-8")

    f1 = open('tweetsfile.txt',encoding="utf-8")
    tweets = f1.read()

    tweets=tweets.lower()

    #items = f.read()

    #items.lower()


    #for tweets

    tokens2 = word_tokenize(tweets)



    tokens2.extend(get_ngrams(tweets,2))

    #print(tokens2)

    #for items

    tokens=[]



    item=f.readline()
    item.lower()

    while(item):
        item=item.lower()
        if item!="\n" and item!="":
            item = item.replace(u'\ufeff', '')
            tokens.append(item.strip())
        item = f.readline()


    #print(tokens)

    '''
    tokens = word_tokenize(line) # Generate list of tokens
    #tokens_pos = pos_tag(tokens)





    tokens2 = word_tokenize(tweets)

    #print(tokens)
    #print(tokens2)
    '''
    f2 = open('req.txt',encoding="utf-8")

    final_list=list(set(tokens).intersection(tokens2))

    return final_list
