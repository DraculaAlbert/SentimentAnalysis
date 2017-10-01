import jieba

#否+程+情

fin = open("test.txt")
fneg = open("neg.txt")
fsent = open("sentiment.txt")
fdgr = open("degree.txt")
fdic = open("newdict.txt",'w')
neg_d = {}
sent_d = {}
dgr_d ={}

line1 = fneg.readline()
while line1:
    line_pos = line1.find("\\")
    line1 = line1[0:line_pos]
    neg_d[line1] = 1
    line1 = fneg.readline()

line2 = fsent.readline()
while line2:
    line_pos = line2.find("\\")
    line2 = line2[0:line_pos]
    sent_d[line2] = 1
    line2 = fsent.readline()

line3 = fdgr.readline()
while line3:
    line_pos = line3.find("\\")
    line3 = line3[0:line_pos]
    dgr_d[line3] = 1
    line3 = fdgr.readline()
fneg.close()
fsent.close()
fdgr.close()

line = fin.readline()
while line:
    seg_list = jieba.cut(line)
    seg_content = (" ".join(seg_list))
    seg_content = seg_content.split()
    pos1 = ''
    pos2 = ''
    pos3 = ''
    for cc in range(0,len(seg_content)):
        pos1 = pos2
        pos2 = pos3
        pos3= seg_content[cc]
        if (neg_d.get(pos1)):
            if(dgr_d.get(pos2)):
                if(sent_d.get(pos3)):
                    write_context = pos1+pos2+pos3+'\n'
                    fdic.write(write_context)
    line = fin.readline()
fin.close()
fdic.close()
