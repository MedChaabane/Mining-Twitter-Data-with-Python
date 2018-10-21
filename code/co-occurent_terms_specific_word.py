search_word = "Obama"
count_search = Counter()
fname = 'trump.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        terms_only = [term for term in preprocess(tweet['text']) 
                      if term not in stop 
                      ]
        if search_word in terms_only:
            count_search.update(terms_only)
print("Co-occurrence for %s:" % search_word)
print(count_search.most_common(20))