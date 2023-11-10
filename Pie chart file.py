# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/content/shopping_trends.csv')
df.info()

import matplotlib.pyplot as plt

gender_counts = df['Gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Gender Distribution')
plt.show()
