bak = open('./bill.txt.bak', 'w', encoding='utf-8')

with open('./bill.txt', encoding='utf-8') as raw:
    for line in raw:
        if line.count('测试') < 1:
            bak.write(line)

    bak.close()
