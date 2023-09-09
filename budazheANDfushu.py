# 算上了负数和不打折的总销量

with open('budazheANDfushu.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    dpbm = content.split()[0]
    xiaoshouzongliang = 0
    for line in content.split('\n'):
        if line.strip():
            if line.split()[2] == '否':
                if line.split()[0] == dpbm:
                    xiaoshouzongliang += float(line.split()[1])
                else:
                    print(dpbm, "\n", xiaoshouzongliang, "\n")
                    with open('budazheANDfushuDEshuchu.txt', 'a', encoding='utf-8') as file:
                        file.write(str(dpbm) + '\n' + str(xiaoshouzongliang) + '\n')
                        file.close()
                    dpbm = line.split()[0]
                    xiaoshouzongliang = float(line.split()[1])


