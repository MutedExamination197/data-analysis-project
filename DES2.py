import pandas as pd
import matplotlib.pyplot as plt

# df=pd.read_excel(r"Excel Files\Dataset.xlsx")

# df_num=df.describe()
# print(df_num.columns)

# for i,col in enumerate(df_num.columns):
#     print(i,col)

data=pd.read_excel(r"Excel Files\Dataset.xlsx")
data_num=data.select_dtypes(include="number")
i=data_num.columns[0:22]

plt.figure(figsize=(10,6))
plt.scatter(data_num[i[3]],data_num[i[12]])
plt.xlabel(i[3])
plt.ylabel(i[12])
plt.show()