#Import Pandas and matplotlib

import pandas as pd
import matplotlib.pyplot as plt

#Create the dataframesusing the json file
df = pd.read_json(r'/rain,json')
print(df)

print('df statistic: ', df.describe())

df.plot(x = 'Month', y = 'Temperature')
df.plot(x = 'Month', y = 'Rainfall')

plt.show()
