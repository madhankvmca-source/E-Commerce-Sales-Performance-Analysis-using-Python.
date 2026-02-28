import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("sales_data.csv")
df["total_amount"]=df["Quantity"]*df["Price"]
category_sale=df.groupby("Category")[["Quantity","total_amount"]].sum().sort_values(by="Quantity",ascending=False)
print(category_sale)
plt.figure()
sea=sns.barplot(data=category_sale, x=category_sale.index, y="total_amount")
for container in sea.containers:
    sea.bar_label(container)
plt.title("category_sale")
plt.show()

