import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("sales_data.csv")
print(df.to_string())
df["total_amount"]=df["Quantity"]*df["Price"]
correlation= df["Quantity"].corr(df["total_amount"])
#print("correlation:",correlation)
plt.figure()
y=sns.scatterplot(data=df, x="Quantity", y="total_amount")
for container in y.containers:
    y.bar_label(container)

plt.title("Quantity vs Revenue")
plt.show()
