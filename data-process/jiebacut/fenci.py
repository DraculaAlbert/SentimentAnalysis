import jieba

fin = open("clothes.txt")
fout = open("res.txt",'w')
line = fin.readline()
while line:
    seg_list = jieba.cut(line)
    write_context = (" ".join(seg_list))
    if write_context:
        write_context = write_context
        fout.write(write_context)
    line = fin.readline()
fin.close()
fout.close()