import pandas as pd
df=pd.read_excel(r"C:\Me\Code\Code\Python\Data_Project\Excel Files\Dataset.xlsx")

df_num=df.describe()
print(df_num.columns)

for i,col in enumerate(df_num.columns):
    print(i,col)