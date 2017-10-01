#this file is used for seach a word in a dictionary

#make dictionary for my dic
fdic = open('dict.txt')
ftest = open('result.txt')
fout = open('mydic.txt','w')
line = fdic.readline()
dictionary = {}
count = 0
while line:
    count +=1
    line_pos = line.find("\\")
    line = line[0:line_pos]
    dictionary[line] = count
    line = fdic.readline()
print(len(dictionary))
fdic.close()

#edit vector.bin
line2 = ftest.readline()
mydictionary = {}
count = 1
while line2:
    tmp = line2.split()
    tmp_size = len(tmp)
    if tmp_size<2:
        line2 = ftest.readline()
        continue
    word = tmp[0]
    value = tmp[1]
    pos = dictionary.get(word)
    pos2 = mydictionary.get(word)
    mydictionary[word] = 1
    if pos:
        if pos2 == None:
            content = str(count)+" "+word + " " + value + '\n'
            count += 1
            fout.write(content)
    line2 = ftest.readline()
print(len(mydictionary))

ftest.close()
fout.close()
