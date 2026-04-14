import pandas as pd
ms_data = pd.read_excel("C:\Me\Code\Code\Python\Data_Project\Excel Files\Dataset.xlsx")
# print(ms_data.head())
# print(ms_data.columns)

# selecting number columns
ms_data_num=ms_data.select_dtypes(include=["number"])
print(ms_data_num.columns)

print(ms_data_num.describe())

print(ms_data_num.dtypes)

print(ms_data_num.columns)




### To access column wise USE
# ms_data_num.iloc[:,1].std()
# iloc["ROW","Columns"]

# Get every Row and a specefic column
# iloc[:,3]
# stops at column with index 2

# Get every row of these specfic column range
# iloc[:,2:5]
# so every row of columns 2->4


# Now get a specif column using a name?
# ms_data_num["EBITDA"]
# ms_data_num[['Revenue', 'Net Profit']]


summary = pd.DataFrame({
    'Mean': ms_data_num.iloc[:,0:23].mean(),
    'Median': ms_data_num.iloc[:,0:23].median(),
    'Mode': ms_data_num.iloc[:,0:23].mode().iloc[0],
    'Std Dev': ms_data_num.iloc[:,0:23].std(),
    'Min': ms_data_num.iloc[:,0:23].min(),
    'Max': ms_data_num.iloc[:,0:23].max()
})
summary.round(2)
summary.to_excel(r"C:\Me\Code\Code\Python\Data_Project\Output.xlsx")


