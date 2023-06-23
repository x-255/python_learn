with open('./bill.txt', encoding='utf-8') as raw:
    ctx = ''
    for line in raw:
        if line.strip().split('，')[4] != '测试':
            ctx += line

    bak = open('./bill.txt.bak', 'w', encoding='utf-8')
    bak.write(ctx)
    bak.close()
