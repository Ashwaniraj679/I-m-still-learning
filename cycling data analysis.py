import numpy as np
import pandas as pd

data = pd.read_csv(r'C:\Users\Ashwani Raj\Desktop\Previous 12 months of Cyclistic trip data\.csv files\202101-divvy-tripdata.csv')
df = pd.DataFrame(data)

print(df)