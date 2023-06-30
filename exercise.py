import re
f = open('names.txt')
data = f.read()

full = re.compile(r'([A-Z][a-zA-Z]+), ([A-Z][A-Za-z-]+)[\s]+([\w-]+[@][a-z]+[.com|.gov]*[.co.se]*)[\s]+([(]*[0-9]{3}[)]*[-]*[\s]*[0-9]{3}[-][0-9]{4})*[\s]*(([A-Z][\w]*([\s]*[A-Z][\w]*)*)), ((([A-Z][\w]*)([A-Z][\w]*)*)[ ]*([A-Z][\w]*)*[.]*)[\s]*([@][a-z]+)')

find_name = full.findall(data)
print(find_name)

print('=================')
print('Full Name/Twitter')
print('=================')
for i in find_name:
    print(f'{i[1]} {i[0]} / {i[12]}')   


# print(data)

# name = re.compile('([A-Z][a-zA-Z]+), ([A-Z][A-Za-z-]+)[\s]+([\w-]+[@][a-z]+[.com|.gov]*[.co.se]*)')
# twitter = re.compile('\B[@][a-z]+')
