import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/content/shopping_trends.csv')
df.info()
import seaborn as sns
plt.figure(figsize=(12, 8))
sns.boxplot(x='Category', y='Purchase Amount (USD)', data=df)
plt.title('Box Plot of Purchase Amount by Category')
plt.xlabel('Category')
plt.ylabel('Purchase Amount (USD)')
plt.show()
