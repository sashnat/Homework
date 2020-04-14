import pandas as pd

data = pd.read_excel(r'https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx')
data["Products"] = data.index
data.index = [i for i in range(len(data))]

dic = dict(zip(data["Products"].values, data["ККал на 100"].values))
print(sorted(dic.items(), key=lambda x: (-x[1], x[0])))
for i in sorted(dic.items(), key=lambda x: (-x[1], x[0])): #(x[0]-->keys, x[1]-->values)
    print(i[0])
print(sorted(dic).index("Паутина"))
print(sorted(dic))

