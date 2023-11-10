# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/content/shopping_trends.csv')
df.info()
import matplotlib.pyplot as plt

plt.hist(df['Age'], bins=20, edgecolor='black')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()
