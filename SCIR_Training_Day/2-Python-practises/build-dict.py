#!/usr/bin/env python
import sys
import pickle
wordcount={}

if __name__=="__main__":
    try:
        fp=open(sys.argv[1],"r",encoding='utf-8')
    except:
        print(sys.stderr,"Failed to open file")
        sys.exit(1)

    for line in fp:
        for word in line.strip().split():
            if word not in wordcount:
                wordcount[word]=0
            wordcount[word]+=1
    # print(wordcount)
    vocab = set([k for k in wordcount if wordcount[k]>2])
    pickle.dump(vocab, open(sys.argv[2], 'wb+'))
    m=pickle.dumps(vocab)
    path = 'D:\\文檔\\GitHub\\scir-training-day\\2-python-practice\\3-max-matching-word-segmentation\\vocab.in'
    n = pickle.load(open(path,'rb+'))
    print(n)


