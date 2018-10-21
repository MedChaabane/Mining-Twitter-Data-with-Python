import operator 
import json
from collections import Counter
from nltk import bigrams 
import math
 
fname = 'trump.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)

        terms_only = [term for term in preprocess(tweet['text']) 
                  if term not in stop 
                  ]

        count_all.update(terms_only)

n_docs=236
p_t = {}
p_t_com = defaultdict(lambda : defaultdict(int))
 
for term, n in count_all.items():
    p_t[term] = n / n_docs
    for t2 in com[term]:
        p_t_com[term][t2] = com[term][t2] / n_docs
        
        
positive_vocab = [
    'strong','good','GOOD','Good','good','good','good','good','good', 'nice', 'great', 'awesome', 'outstanding',
    'fantastic', 'terrific', ':)', ':-)', 'like', 'love',

]
negative_vocab = [
    'hell','dead','crime','racist','DISASTER','bad','angry','fake','FAKE','loser','TERRIBLE','stupid','stupidity',
    'dumb','worst', 'terrible', 'crap', 'useless', 'hate', ':(', ':-(','weak',

]


pmi = defaultdict(lambda : defaultdict(int))
for t1 in p_t:
    for t2 in com[t1]:
        denom = p_t[t1] * p_t[t2]
        pmi[t1][t2] = math.log2(p_t_com[t1][t2] / denom)
 
semantic_orientation = {}
for term, n in p_t.items():
    positive_assoc = sum(pmi[term][tx] for tx in positive_vocab)
    negative_assoc = sum(pmi[term][tx] for tx in negative_vocab)
    semantic_orientation[term] = positive_assoc - negative_assoc
semantic_sorted = sorted(semantic_orientation.items(), 
                         key=operator.itemgetter(1), 
                         reverse=True)
top_pos = semantic_sorted[:20]
top_neg = semantic_sorted[-20:]
print(top_pos)
print(top_neg)