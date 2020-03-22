import re
import base64

regex = r"src=\"(.+\.jpg)\""

file = input("Enter filename: ")

raw = open(file,'r').read()
filesList = []
matches = re.finditer(regex, raw, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        filesList.append( match.group(groupNum))

for index in range(0, len(filesList) ):
    print(filesList[index])
    img = open(filesList[index], "rb")
    encodeImg = base64.b64encode(img.read())
    raw = raw.replace(filesList[index],"data:image/png;base64, {base}".format( base = encodeImg.decode("utf-8")) )
    
with open(file.replace('.html','_base64.html'), 'a') as out:
    out.write(raw)