fdic = open('mydic.txt')
fneg = open('test.txt')
fsvm = open('svm_data.txt','w')
dict_number = {}
dict_value = {}

line = fdic.readline()
while line:
    tmp = line.split()
    if(len(tmp)<3):
        line = fdic.readline()
        continue
    number = tmp[0]
    word = tmp[1]
    value = tmp[2]
    dict_number[word] = number
    dict_value[word] = value
    line = fdic.readline()
fdic.close()

line2 = fneg.readline()
while line2:
    line2_content = line2.split()
    content = "-1"
    for i in range(0,len(line2_content)):
        data = line2_content[i]
        if dict_number.get(data):
            tmp = " "
            tmp += str(dict_number.get(data))+":"+str(dict_value.get(data))
            content += tmp
    content += "\n"
    fsvm.write(content)
    line2 = fneg.readline()
fsvm.close()
fneg.close()
