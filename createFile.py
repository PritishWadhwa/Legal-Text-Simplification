import sys
argList = sys.argv
fileName = argList[1]
file = open(fileName, 'r+')
text = [file.read()]
outputText = []
flag = 0
start = 0
for i in text[0]:
    if start == 0 and i == '\n':
        continue
    if flag == 1:
        flag = 0
        if i == '\n':
            outputText.append('\n\n')
            continue
        else:
            outputText.append('\\N')
    if i == '.':
        start = 1
        outputText.append(' \\F')
    elif i == '\n':
        start = 1
        flag = 1
    else:
        start = 1
        outputText.append(i)
file.seek(0)
file.writelines(outputText)
file.close()
