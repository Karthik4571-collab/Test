import numpy as np
from operator import add
from functools import reduce
import pandas as pd

coding={'subject':['python','java'],"amount":[1000,2000]}
df=pd.DataFrame(coding)
print(df)

print("\n map operation to multiply amount by 2\n")
df['amount'] = df['amount'].map(lambda x: x * 2)
print(df)
print("\n")
print("\n operation of filters to display only subject column \n")
df2=df.filter(items=['subject'])
print(df2)
print("\n reduce operation to find total amount\n")
print(reduce(add,df.amount))





