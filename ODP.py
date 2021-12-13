import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv('marketing_campaign.csv', sep='\t')

print(data.head())

grouped_id_data = data.groupby('MntSweetProducts')
grouped_id_data_income = grouped_id_data['MntFishProducts']
mean_grouped_id_data_income = grouped_id_data['MntFishProducts'].mean()
print(mean_grouped_id_data_income.head())

l,a = list(set(data["Marital_Status"])),[]
for i in range(len(l)):
    a.append(data["Marital_Status"].to_list().count(l[i]))
plt.bar(x=range(len(l)),height = a)
plt.xticks(labels=l,ticks=range(len(l)), rotation=90)
plt.show()

age = 2021-data.Year_Birth.to_numpy()
l, a = list(set(age)), []
for i in range(len(l)):
    a.append(list(age).count(l[i]))
plt.figure(figsize=(12, 4))
plt.bar(x=range(0, len(l)*3, 3), height=a)
plt.xticks(labels=l,ticks=range(0, len(l)*3,3),rotation=90)
plt.show()

sns.displot(data=data, y="Kidhome", x="Education")
plt.show()

sns.histplot(x=data.Income, kde=True)
plt.show()

data.Income.describe()
print(data.Income.describe())

income = data.loc[data['Income'] < 300000]['Income']
sns.histplot(x=income, kde=True)
plt.show()

fig, axes = plt.subplots(2, 2, sharex=True, figsize=(10,5))
fig.suptitle('Kids Home Vs Amount Spent on Purchases by Channel')
sns.regplot(y='NumWebPurchases', x='Kidhome', data=data, ax=axes[0,0])
sns.regplot(y='NumDealsPurchases', x='Kidhome', data=data, ax=axes[0,1])
sns.regplot(y='NumCatalogPurchases', x='Kidhome', data=data, ax=axes[1,0])
sns.regplot(y='NumStorePurchases', x='Kidhome', data=data, ax=axes[1,1])
plt.show()
