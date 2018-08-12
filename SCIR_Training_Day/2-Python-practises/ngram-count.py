#!/usr/bin/env python

class NGram(object):

    def __init__(self,sentence,n):
        # n is the order of n-gram language model
        self.n = n
        self.sentence = sentence
        self.unigram = {}
        self.bigram = {}

    # scan a sentence, extract the ngram and update their
    # frequence.
    #
    # @param    sentence    list{str}
    # @return   none
    def scan(self):
        if self.n == 1:
            try:
                fpo = open('data.uni','w')
            except IOError:
                print(sys.stderr[2],'failed to open file')
                sys.exit(1)
            for i in self.unigram:
                fpo.write(i+'\t'+str(self.unigram[i])+'\n')
            print('unigram done!')
            fpo.close()
        if self.n ==2:
            try:
                fpo = open('data.bi','w')
            except IOError:
                print(sys.stderr[2],'failed to open file')
                sys.exit(1)
            for i in self.bigram:
                fpo.write(str(i)+'\t'+str(self.bigram[i])+'\n')
            print('bigram done!')
            fpo.close()
        # file your code here

    # caluclate the ngram of the words
    #
    # @param    words       list{str}
    # @return   int         count of the ngram
    def ngram(self):
        if self.n == 1:
            for i in self.sentence:
                try:
                    self.unigram[i] +=1
                except KeyError:
                    self.unigram[i] = 1
                    
        if self.n ==2:
            for i in range(len(self.sentence)-1):
                    word_pair = ()            
                    try:
                        word_pair = (self.sentence[i],self.sentence[i+1])
                        self.bigram[word_pair] += 1
                    except KeyError:
                        self.bigram[word_pair] = 1
        
        return self.unigram,self.bigram



def read_sentence(fp):
    sentence = []
    line = [i.strip() for i in fp.readlines()]

    # 给原始文本添加起始符和终止符
    for index,i in enumerate(line):
        # line[index] = line[index].strip(r'\n')
        line[index] = '<s> '+ i +' </s> '

    if len(line) != 0:
        sentence = (''.join(line).split())
    else:
        pass
    
    return sentence




if __name__=="__main__":
    import sys
    # print >> sys.stderr, "library is not runnable"
    try:
        fpi = open(sys.argv[1],'r')
    except IOError:
        print(sys.stderr,"failed to open file")
        sys.exit(1)
    
    content = read_sentence(fpi)

    unigram = NGram(content,1)
    bigram = NGram(content,2)

    unigram.ngram()
    bigram.ngram()
    unigram.scan()
    bigram.scan()


    fpi.close()




