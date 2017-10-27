fin = open("old.txt")
fout = open("new.txt",'w')
dict_word = []
dict_value = []
line = fin.readline()
while line:
    tmp = line.split()
    if len(tmp) < 2:
        line = fin.readline()
        continue
    # different, related to the dictionary
    word = tmp[1]
    value = float(tmp[2])
    dict_value.append(value)
    dict_word.append(word)
    line = fin.readline()
fin.close()
#print (dict_word)
#print (dict_value)

cc = 0

while len(dict_value):
    cc += 1
    if cc%5000 == 0:
        print(cc)
    pos = dict_value.index(max(dict_value))
    print(max(dict_value))
    v = dict_value.pop(pos)
    d = dict_word.pop(pos)
    content = str(cc) + " " + d+"\n"
    #print(content)
    fout.write(content)