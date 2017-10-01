#import jieba
import jieba.posseg as pseg

fin = open("clothes.txt")
fn = open("n.txt",'w')
fv = open("v.txt",'w')
fadj = open("adj.txt",'w')
fadv = open("adv.txt",'w')
nd = {}
vd = {}
adjd ={}
advd = {}
line = fin.readline()
while line:
    words = pseg.cut(line)
    for word,flag in words:
        if(flag=='v'):
            if(vd.get(word)==None):
                vd[word] = 1
                content = word + '\n'
                fv.write(content)
        elif(flag=='n'):
            if (nd.get(word)==None):
                nd[word] = 1
                content = word + '\n'
                fn.write(content)
        elif (flag == 'a'):
            if (adjd.get(word)==None):
                adjd[word] = 1
                content = word + '\n'
                fadj.write(content)
        elif (flag == 'd'):
            if (advd.get(word)==None):
                advd[word] = 1
                content = word + '\n'
                fadv.write(content)
        else:
            continue
    line = fin.readline()
fin.close()
fn.close()
fv.close()
fadj.close()
fadv.close()