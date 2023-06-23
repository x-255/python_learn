with open('./bill.txt', encoding='utf-8') as raw:
    ctx = ''
    for line in raw:
        if line.count('测试') > 0:
            continue
        ctx += line

    bak = open('./bill.txt.bak', 'w', encoding='utf-8')
    bak.write(ctx)
    bak.close()
