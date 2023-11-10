# -*- coding: utf-8 -*-
"""
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/content/shopping_trends.csv')
df.info()

import matplotlib.pyplot as plt

plt.scatter(df['Review Rating'], df['Purchase Amount (USD)'])
plt.title('Scatter Plot of Review Rating vs. Purchase Amount')
plt.xlabel('Review Rating')
plt.ylabel('Purchase Amount (USD)')
plt.show()
