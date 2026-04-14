import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_excel(r"C:\Me\Code\Code\Python\Data_Project\Excel Files\Dataset.xlsx")
data_num=data.select_dtypes(include=["number"])

# a=pd.DataFrame(data_num.columns)
# # a.to_excel("C:\Me\Code\Code\Python\Data_Project\help.xlsx")

a=data_num.columns

print(a[0:22])
## USed GPT to understand how to build a loop
#### HISTOGRAMS
for col in a[0:23]:
    plt.figure()
    data_num[col].hist()

    plt.title(f"{col} Distribution")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.savefig(f"C:\Me\Code\Code\Python\Data_Project\Histogram Plots\{col}_hist.png")
    plt.close()


# ##### Boxplots
for col in a[0:23]:
    plt.figure()
    plt.boxplot(data_num[col])
    plt.title(f"{col} Box Plot")
    plt.savefig(f"C:\Me\Code\Code\Python\Data_Project\BoxPlots\{col}_boxplots.png")
    plt.close()

### Correlation 
corr=data_num.iloc[:,0:23].corr()

plt.figure()
sns.heatmap(corr, annot=True)

plt.title("Correlation Heatmap")
plt.savefig("C:\Me\Code\Code\Python\Data_Project\Correlation Heatmap\Correlation Heatmap.png")





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
    plt.figure()
    plt.scatter(data_num[i[0]], data_num[i[1]])
    x=(f"{i[0]} vs {i[1]}")
    plt.title(x)
    plt.xlabel(f"{i[0]}")
    plt.ylabel(f"{i[1]}")
    plt.savefig(r"Python\Data_Project\Scatter plots\\" + x + ".png")
    plt.close()