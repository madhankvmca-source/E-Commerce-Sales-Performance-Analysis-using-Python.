import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("sales_data.csv")
payment=df["Payment_Method"].value_counts()
print(payment)
plt.figure()
r=sns.countplot(data=df,x="Payment_Method")
for container in r.containers:
    r.bar_label(container)
plt.title("payment used high")
plt.show()



