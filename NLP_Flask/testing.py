a = "this is           a cars"

clean = a.split()
print(" ".join(a.split()))

from stemming.porter2 import stem

red_text = [stem(word) for word in clean]
print(red_text)

import pandas as pd

data = pd.read_csv("input.csv")
col_name = 'text'
data["jimi"] = [1,2,3]
print(data)
