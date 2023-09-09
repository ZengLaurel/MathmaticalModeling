# 打折

# 初始化各类别的销售总量
categories_sales = {"花菜类": 0, "花叶类": 0, "辣椒类": 0, "茄类": 0, "食用菌": 0, "水生根茎类": 0}

# 读取数据库1.txt的内容，并创建一个字典以加快检索
database1_dict = {}
with open('database1.txt', 'r', encoding='utf-8') as file1:
    for line1 in file1:
        parts1 = line1.split()
        if len(parts1) >= 4:
            dpbm1 = parts1[0]
            category1 = parts1[3]
            database1_dict[dpbm1] = category1

# 读取database2.txt的内容，计算销售总量并合并到对应类别
with open('database2DAZHE.txt', 'r', encoding='utf-8') as file2:
    for line2 in file2:
        parts2 = line2.split()
        if len(parts2) >= 2:
            dpbm2 = parts2[0]
            sales = float(parts2[1])
            if dpbm2 in database1_dict:
                category2 = database1_dict[dpbm2]
                if category2 in categories_sales:
                    categories_sales[category2] += sales

# 输出各类别的销售总量
for category, sales in categories_sales.items():
    print(f"{category}: {sales}")

# 计算总销售总量
total_sales = sum(categories_sales.values())
print(f"打折总销售总量: {total_sales}")