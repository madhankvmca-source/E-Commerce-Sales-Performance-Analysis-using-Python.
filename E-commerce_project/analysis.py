import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales_data.csv",na_values=["None"])

print(df.to_string())
#df.head() #Shows the first 5 rows of the dataset.
#df.info() #Gives complete summary of dataset.
#df.describe() #Gives statistical summary of numerical columns.
nll=df.isnull().sum() #Checks missing values in each column.

dup=df.drop_duplicates(inplace=True)#To remove duplicate rows from the dataset.(inplace=True)#It directly modifies the original dataframe (df).
#print(dup)
drp=df.dropna(inplace=True)#To remove rows that contain missing values (NaN).
#print(drp)
df['Total_Sales'] = df['Quantity'] * df['Price']
#print(df['Total_Sales'])
srt=df.sort_values("Price",ascending=False)
#print(srt)
total_price=df["Price"].sum()
#print(total_price)
top_product=df.groupby("Product")["Price"].sum().sort_values(ascending=False).head(5)
#print(top_product)
citi_sales=df.groupby("City")["Price"].sum().sort_values(ascending=False).head(2)
#print(citi_sales)
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
#print(df['Order_Date'] )
df['Month'] = df['Order_Date'].dt.month
#print(df['Month'])

monthly_sales = df.groupby('Month')['Price'].sum()
#print(monthly_sales )


#1) TOTAL REVENUE
df["total_amount"]=df["Quantity"]*df["Price"]
#print(df["total_amount"])
total_revenue=df["total_amount"].sum()
#print("1)Total_Revenue:",total_revenue)

#2)Which city generates the highest revenue?
cities=df.groupby("City")["Price"].sum().sort_values(ascending=False).head(1)
#print("2)city:",cities)

#3)Which product category sells the most (by quantity)?**
category_sales=df.groupby("Category")["Quantity"].sum().sort_values(ascending=False)
category_sale=df.groupby("Category")[["Quantity","total_amount"]].sum().sort_values(by="Quantity",ascending=False)
#print(category_sales)
#print(category_sale)

#4) Which payment method is most used?**
payment=df["Payment_Method"].value_counts().head(1)
#print(payment)

#5) What is the average order value?
avg_val=df["total_amount"].mean()
#print("average order values:",avg_val)

#6) Monthly Sales Trend Analysis
df["Order_Date"]=pd.to_datetime(df["Order_Date"])
df["Month"]=df["Order_Date"].dt.month
Monthly_Sales=df.groupby("Month")["total_amount"].sum().sort_values(ascending=False)
#print(Monthly_Sales)

#7) Which customer spent the most?
custom=df.groupby("Customer_Name")["total_amount"].sum().sort_values(ascending=False).head(1)
#print(custom)

#8) What is the highest single order value?
highest= df["Price"].max()
#print(highest)

#9) Which month had highest sales?
Mont=df.groupby("Month")["total_amount"].sum().sort_values(ascending=False).head(1)
#print(Mont)

month=monthly_sales.idxmax()
#print(month)

#10)Top 3 most expensive products sold
expensive=df.sort_values(by="Price", ascending=False)[["Product","Price"]].head(3)
#print(expensive)

#11) total orders

total_orders=df["Order_ID"].nunique()
#print(total_orders)

#12) Do higher quantities mean higher revenue?
correlation= df["Quantity"].corr(df["total_amount"])
#print("correlation::",correlation)

#13) quarter=This extracts the quarter(map from jan-mar,arp-june etc..) number from each date.
df["Quarter"] = df["Order_Date"].dt.quarter
quarter_sales = df.groupby("Quarter")["total_amount"].sum()
#print(quarter_sales)

#14) What percentage of revenue comes from Electronics?

category_revenue = df.groupby("Category")["total_amount"].sum()
total_revenue = df["total_amount"].sum()

electronics_percentage = (category_revenue["Electronics"] / total_revenue) * 100
#print(electronics_percentage)

#15)Which city prefers COD more?
cod_city = df[df["Payment_Method"] == "COD"]["City"].value_counts()
#print(cod_city)

#16) Which month had the lowest sales?
df["Month"] = df["Order_Date"].dt.month
monthly_sales = df.groupby("Month")["total_amount"].sum()
lowest_month = monthly_sales.idxmin()
#print(lowest_month)

#17)Is there seasonality in this data?
quarter_sales = df.groupby(df["Order_Date"].dt.quarter)["total_amount"].sum()
print(quarter_sales)




















 
