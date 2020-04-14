import pandas as pd
import numpy as np
df1 = pd.read_excel(r'https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx ', sheet_name="Справочник")
df1["Продукт"] = df1.index
df2 = pd.read_excel(r'https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx ', sheet_name="Раскладка", index_col=False)
df3 = df1.merge(df2)
df3=df3.fillna(0)
func = lambda x: np.asarray(x) * np.asarray(df3["Вес в граммах"]) * 0.01
df4 = df3[["ККал на 100","Б на 100", "Ж на 100","У на 100"]].apply(func)
df5 = df4.sum(axis=0)
res = ' '.join(str(int(i)) for i in df5.values)
print(res)
