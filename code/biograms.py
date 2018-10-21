from nltk.corpus import stopwords
import string
from nltk import bigrams 

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
fname = 'trump.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        terms_stop = [term for term in preprocess(tweet['text']) 
                      if term not in stop 
                      and not term.startswith(('#', '@'))]
        terms_bigram = bigrams(terms_stop)
        count_all.update(terms_bigram)
    print(count_all.most_common(30))  