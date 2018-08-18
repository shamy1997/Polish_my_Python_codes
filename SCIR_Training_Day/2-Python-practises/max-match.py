#!/usr/bin/env python
import pickle
import sys

def max_match_segment( line, dic ):
    maxlen = 0
    for i in dic:
        if len(i) > maxlen:
            maxlen = len(i)
        else:
            continue
    # print(maxlen)
    # 确定最大词长

    s1 = line[:maxlen]
    result = []
    log = 0

    for i in range(len(line)):
        while s1 not in dic:
            if len(s1)>1:
                s1 = s1[:-1]
            elif len(s1) <= 1 and len(line)>maxlen:
                result.append(s1)
                line = line[1:]
                s1 = line[:maxlen]
                break
            elif len(s1) <= 1 and len(line) <= maxlen:
                result.append(s1)
                line = line[1:]
                s1 = line
                break

        else:
            result.append(s1)
            l_index = line.index(s1)

            line = line[l_index+len(s1):]
            s1 = line[:maxlen]

    return result



    
if __name__=="__main__":
    try:
        fpi=open(sys.argv[1], "r")
    except:
        print(sys.stderr, "failed to open file")
        sys.exit(1)

    try:
        dic = pickle.load(open(sys.argv[2],'rb+'))
    except:
        print(sys.stderr, "failed to load dict")
        sys.exit(1)

    for line in fpi:
        print("\t".join(max_match_segment(line.strip(), dic)))
        

