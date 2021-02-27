import sys
argList = sys.argv
fileName = argList[1]
file = open(fileName, 'r+')
text = [file.read()]
outputText = []
flag = 0
for i in text[0]:
    if flag == 1:
        flag = 0
        if i == '\n':
            outputText.append('\n\n')
            continue
        else:
            outputText.append('\\N')
    if i == '.':
        outputText.append(' \\F')
    elif i == '\n':
        flag = 1
    else:
        outputText.append(i)
file.seek(0)
file.writelines(outputText)
file.close()
annFile = fileName[:-3] + 'ann'
newFile = open(annFile, 'w')
newFile.close()
