import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_excel(r"Excel Files\Dataset.xlsx")
data_num=data.select_dtypes(include=["number"])

# a=pd.DataFrame(data_num.columns)
# # a.to_excel("C:\Me\Code\Code\Python\Data_Project\help.xlsx")

a=data_num.columns
# # print(a)
# for i, col in enumerate(a):
#     print(i,col)
# print(a[0:22])
# ## USed GPT to understand how to build a loop
# #### HISTOGRAMS
for col in a[0:22]:
    plt.figure(figsize=(10,6))
    data_num[col].hist()

    plt.title(f"{col} Distribution")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.savefig(f"Histogram Plots\{col}_hist.png",dpi=300)
    plt.close()


# ##### Boxplots
for col in a[0:22]:
    plt.figure(figsize=(10,6))
    plt.boxplot(data_num[col])
    plt.title(f"{col} Box Plot")
    plt.savefig(f"BoxPlots\{col}_boxplots.png",dpi=300)
    plt.close()

### Correlation 
corr=data_num.iloc[:,0:22].corr()

plt.figure(figsize=(12,10))
sns.heatmap(corr, annot=True)

plt.title("Correlation Heatmap")
plt.savefig("Correlation Heatmap\Correlation Heatmap.png",dpi=300)





#### profit margin distribution
plt.figure()

sns.histplot(data_num['Profit margin'], kde=True)

plt.title("Distribution of Profit Margin")
plt.xlabel("Profit Margin")
plt.ylabel("Frequency")

plt.show()



### Scatter plot
plt.figure()

pairs = [
    ('Revenue', 'Net Profit'),
    ('Revenue', 'Total Cost'),
    ('Total Cost', 'Net Profit'),
    ('Employee Count', 'Revenue'),
    ('Employee Count', 'Total Cost'),
    ('Revenue', 'Profit margin'),
    ('Cost Per employee', 'Profit margin')
]

for i in pairs:
    plt.figure(figsize=(10,6))
    plt.scatter(data_num[i[0]], data_num[i[1]])
    x=(f"{i[0]} vs {i[1]}")
    plt.title(x)
    plt.xlabel(f"{i[0]}")
    plt.ylabel(f"{i[1]}")
    filename = f"plots/{i[0].replace(' ', '_')}_vs_{i[1].replace(' ', '_')}.png"
    plt.savefig(filename, dpi=300)
    plt.close()