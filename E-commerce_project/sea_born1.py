import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("sales_data.csv")
df["total_amount"]=df["Quantity"]*df["Price"]
city_revenue=df.groupby("City")["total_amount"].sum().sort_values(ascending=False)
plt.figure()
t=sns.barplot(x=city_revenue.index, y=city_revenue.values)
for container in t.containers:
    t.bar_label(container)
plt.xticks(rotation=45)
plt.title("city_revenue")
plt.show()

