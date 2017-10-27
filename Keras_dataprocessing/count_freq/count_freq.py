fpos = open('pos.txt')
fneg = open('neg.txt')
fdict = open('ddd.txt')
#fout = open('count_ori.txt','w')
fout = open('soltv2.txt','w')


dict_word = []
dict_count = []
line = fdict.readline()
#构建字典
while line:
    tmp = line.split()
    if len(tmp) ==0 :
        line = fdict.readline()
        continue
    word = tmp[0]
    dict_word.append(word)
    dict_count.append(0)
    line = fdict.readline()
fdict.close()

#统计正类样本词频
line2 = fpos.readline()
ccc = 0
while line2:
    ccc += 1
    if ccc%1000 == 0:
        print(ccc)
    content = line2.split()
    if len(content)<2:
        line2 = fpos.readline()
        continue
    for cc in range(0,len(content)):
        if content[cc] in dict_word:
            pos = dict_word.index(content[cc])
            dict_count[pos] += 1
    line2 = fpos.readline()

#统计负类样本词频
ccc = 0
line3 = fneg.readline()
while line3:
    ccc += 1
    if ccc%1000 == 0:
        print(ccc)
    content = line3.split()
    if len(content)<2:
        line3 = fneg.readline()
        continue
    for cc in range(0,len(content)):
        if content[cc] in dict_word:
            pos = dict_word.index(content[cc])
            dict_count[pos] += 1
    line3 = fneg.readline()

fpos.close()
fneg.close()

c_count = 0
while len(dict_word):
    c_count += 1
    pos = dict_count.index(max(dict_count))
    ww = dict_word.pop(pos)
    freq = dict_count.pop(pos)
    write_content = str(c_count)+' '+str(ww)+' '+str(freq)+'\n'
    fout.write(write_content)
fout.close()
