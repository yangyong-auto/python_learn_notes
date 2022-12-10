import re

f = open(r're_module/sample.txt','rt',encoding='utf-8')
content = f.read()

p = re.compile(r'(\d.*)(万)')

for one in p.findall(content):
    print(one)


