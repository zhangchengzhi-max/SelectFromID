f = open('a.txt', encoding='utf-8')
c = open('cheshenyu.txt', 'w')

for i in f.readlines():
    if "车身域" in i:
        c.write(i)
f.close()
c.close()