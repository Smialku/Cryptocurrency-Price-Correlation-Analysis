import pandas as pd
from pandas import read_csv
import seaborn as sns
import matplotlib.pyplot as plt

crypto_files = ["btc-usd-max.csv","xrp-usd-max.csv","doge-usd-max.csv","eth-usd-max.csv","shib-usd-max.csv","sol-usd-max.csv"]

final_df = pd.DataFrame()
for file in crypto_files:

    df = pd.read_csv(file)
    crypto_name = file.split("-")[0]
    col = df['price']
    last_365 = col.iloc[-365:].reset_index(drop=True)
    final_df[crypto_name] = last_365


correlation_matrix = final_df.corr()


plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
plt.title("Correlation matrix")
plt.show()





