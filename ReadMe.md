This Project is contains a baisc analysis of the relationship between various company metrics. For the internal cost, data has been spoofed using the cost structure of another service company
Since having reliable financial data was important, the companies selected have been restriced to publicly traded companies whose final account statements are readily available

## Tools Used
Python
Pandas
Matplotlib
Seaborn

# Graphs and Plots
## Scatter Plots
### Revenue Vs Net Profit
<img width="3000" height="1800" alt="Revenue_vs_Profit_margin" src="https://github.com/user-attachments/assets/c15a7f0e-06fa-4a32-b51d-f66c22debf9a" />
The above graph suggests a strong positive correlation between Revenue and Net Profit
Companies with higher revenue generally tend to have higher profits.
Suprisingly, 42 of the 51 companies lie between profit margins of 0 and 20% of profit margin

### Revenue vs Total Cost
<img width="3000" height="1800" alt="Revenue_vs_Total_Cost" src="https://github.com/user-attachments/assets/0e61b8d9-b001-4fa5-a1f5-47b2c26e9eca" />
Revenue and total cost show a strong linear relationship.
This suggests that scaling operations comes with proportional cost increases.

### Total Cost vs Net Profit
<img width="3000" height="1800" alt="Total_Cost_vs_Net_Profit" src="https://github.com/user-attachments/assets/69b416cd-994c-4308-9d46-4e624eee4b2f" />
Higher costs are generally associated with higher profits, but not always proportionally.
Some companies exhibit high costs but comparatively lower profits, indicating inefficiencies.

### Employee Count vs Revenue
<img width="3000" height="1800" alt="Employee_Count_vs_Revenue" src="https://github.com/user-attachments/assets/34677401-31f4-4ac1-9e78-1204d89d828a" />
There is a positive correlation between employee count and revenue, therefore larger companies are able to employ more eployees, and thus generate more revenue
However some companeis seem to have large employee basis but aren't able to generate high revenue
Majority of the companies are are clustered to the left side, indicating that it is relatively easier to employ less and generate less revune then the opposite

### Employee Count vs Total Cost
<img width="3000" height="1800" alt="Employee_Count_vs_Total_Cost" src="https://github.com/user-attachments/assets/91606ac3-53c8-434a-bab6-2aee6c51c3e6" />
A strong positive relationship exists between employee count and total cost.
Workforce size is a major driver of company expenses.

### Cost per Employee vs Profit Margin
<img width="3000" height="1800" alt="Cost_Per_employee_vs_Profit_margin" src="https://github.com/user-attachments/assets/e5b8445c-fed4-4447-9ba2-04a778ee1d98" />
There is no clear linear relationship between cost per employee and profit margin.
Majority of values are conentrated on the left hand side, indicating that some companies are able to better utilize the human resource talent, while some companies with the same number of workforce are unable to capitalise on the human talent
Others show high per eomployee costs with relativley similiar margins, indicating inefficiency.

### Revenue vs Profit Margin
<img width="3000" height="1800" alt="Revenue_vs_Profit_margin" src="https://github.com/user-attachments/assets/a889e0e0-af7d-4843-ac2c-08d612e4e058" />
Revenue generated seems to have little effect on the profit margin.
Both small and large companies show a wide range of profit margins.
This indicates efficiency in utilization of resources, is a batter metric in predicting net profits and profit margins  


## Histograms
### 1. Revenue Distribution
<img width="3000" height="1800" alt="Revenue_hist" src="https://github.com/user-attachments/assets/54e12c21-7c0c-43e1-a8dc-4cec0aa9871c" />
Most companies fall in the lower revenue range, with only a few companies being able to generate higher revenue.

### 2. Profit Margin Distribution
<img width="3000" height="1800" alt="Profit margin_hist" src="https://github.com/user-attachments/assets/9873cc7c-5989-4347-b16f-2e84c108be75" />
The Profit Margin Distribution is normally distributed
Majority of companies operate within 5%–20% profit margins
Some companies show negative margins, indicating losses
A few high performers exceed 30% margins

### 3. Net Profit Distribution
<img width="3000" height="1800" alt="Net Profit_hist" src="https://github.com/user-attachments/assets/99e7d714-d204-4525-abdd-82b749846b3c" />
Similar to revenue, profits are heavily skewed.
Most companies generate modest profits, with only a Few firms dominate total profitability

### 4. Return on ROE
<img width="3000" height="1800" alt="ROE_hist" src="https://github.com/user-attachments/assets/ebe28201-4776-4c29-b7d0-31abfcdfbfdc" />
The ROE distribution seems to be a skewed normal distribution
Most companies exhibit moderate positive ROE values, while a smaller number 
of firms show negative returns.
This shows that while there ar ea majority of profitable firms, there seems to be a few notable underperformers in the industry
It is also worth noting the gap between the companies offering high ROE and the ones offering in the range of (0.50-0.75)

### 5. Cost Efficiency (Cost per Employee)
<img width="3000" height="1800" alt="Cost Per employee_hist" src="https://github.com/user-attachments/assets/0015d440-1246-4b4c-9960-f679651c46f9" />
Large variation across companies
Some companies operate with very high cost per employee

## Heatmap
<img width="3600" height="3000" alt="Correlation Heatmap" src="https://github.com/user-attachments/assets/e950556d-8005-4a92-a6a4-c2157416ef5d" />
Revenue, Net Profit, EBITDA, and Market Capitalization are highly positively correlated, indicating that future growth of the company is strongly predicted by these factors 
Employee count also shows a strong positive relationship with revenue and cost, suggesting that larger organizations tend to generate higher throughput.
It is noteworthy, that ROE has a weak relation with profit metrics such as revenue and Net profit
This indicates that operational efficincy is an impotant metric to consider in deciding the overall profitability of the organisation, simply scale of the business is not a string indicator of profitability

## Conclusion
The following hoghlights could be drawn by me
1. A few players dominate the market, and that to with a wide margin. This is shown by the heavily skewed distributions of profitability metrics.

2. Even though the profitability metrics are highly skewed the distribution of moderate profits is more even.

3. Scatter plots and correlation plots show strong positive relationships between Revenue, Net Profit, Total Costs and Market Capitalization. This shows that the industry market tends to favour bigger companies more.

4. Despite the market favouring large companies more,  the individual profitability of the firm is more dictated by factors like efficiency, making profitability a metric independant of scale

5. There seems to be a string prsence of outliers, who are performing exceptionally well and by a wide margin. Covnersely the underperformers are more closer to the average than the overperformers.
   This suggests the presence of a potential lower bound on underperformance, possibly due to market constraints. However, the high-performing firms are able to scale and grow with no such clear upper-bound for them.
