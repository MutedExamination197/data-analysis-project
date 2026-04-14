import pandas as pd
df=pd.read_excel(r"Excel Files\Dataset.xlsx")

df_num=df.describe()
print(df_num.columns)

for i,col in enumerate(df_num.columns):
    print(i,col)