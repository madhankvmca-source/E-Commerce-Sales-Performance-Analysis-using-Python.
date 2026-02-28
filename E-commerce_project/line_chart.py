import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("sales_data.csv")
print(df.to_string())

df["Order_Date"]=pd.to_datetime(df["Order_Date"])
print(df["Order_Date"])
df["month"]=df["Order_Date"].dt.month
monthly_sales = df.groupby('month')['Price'].sum()
# line CHARTS

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Price")
plt.show()
