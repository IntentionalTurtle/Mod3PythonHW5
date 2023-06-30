import re

f = open('regex_test.txt')
data = f.readlines()
names = re.compile('([A-Z][a-zA-Z]+)[ ]*([A-Z]([\w]+)*)*[ ]*([A-Z][\w]+)')

# print(data)
for i in data:
    found = names.findall(i)
    if found == []:
        print('None')
    else:
        print(f'{found[0][0]} {found[0][1]} {found[0][3]}')
    




