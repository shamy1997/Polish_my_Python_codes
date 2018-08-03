#!/usr/bin/env python
import sys

def read_instance(fp):
    sentence = []
    while True:
        line = fp.readline()
        if not line:
            yield sentence
            break

        line = line.strip()

        if len(line) == 0:
            yield sentence
            sentence = []
        else:
            sentence.append( line.split() )


#思路：反序遍历，将B作为输出序列的信号；
def bi2words(chars):
    items = list(reversed(chars))
    segs = []
    #print('items is ',items)
    content = []
    for word in items:
        # print('word is',word)
        content.append(word[0])
        # print('content is',content)
        if word[1] == "B":
            segs.append(''.join(reversed(content)))
            content = []
        else:
            continue
    return list(reversed(segs))





if __name__=="__main__":
    try:
        fpi = open(sys.argv[1], "r")
    except IOError:
        print(sys.stderr, "failed to open file.")
        sys.exit(1)

        
    try: 
        fpo = open(sys.argv[2], "w")
    except IOError:
         print(sys.stderr, "failed to open file.")
         sys.exit(1)

    for sentence in read_instance(fpi):
        for i in bi2words(sentence):
            fpo.write(i+' ')
        fpo.write('\n')
        print('done!')
    fpi.close()
    fpo.close()

