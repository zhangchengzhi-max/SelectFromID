f = open('a.txt', encoding='utf-8')

c = open('jiayinhao.txt', 'w')

for i in f.readlines():
    i = i.strip()
    c.write('"'+i+'"'+',')
f.close()
c.close()