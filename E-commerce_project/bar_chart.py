import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("sales_data.csv")
print(df.to_string())
top_product=df.groupby("Product")["Price"].sum().sort_values(ascending=False).head(5)
print(top_product)

#bar charts
plt.figure()
ax=top_product.plot(kind='bar')
for container in ax.containers:
    ax.bar_label(container)

plt.title("Top 5 Products")
plt.xlabel("Price")
plt.show()