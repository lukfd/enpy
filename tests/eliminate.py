import pandas as pd

df = pd.read_csv('./edges.csv')
df.drop_duplicates(inplace=True)
df.to_csv('./cleaned_edges.csv', index=False)