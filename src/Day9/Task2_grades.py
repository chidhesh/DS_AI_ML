import pandas as pd

grades=pd.Series([85, None, 92, 45, None, 78, 55])
df=pd.DataFrame(grades)

print("Original Full Scores :",grades)
null=pd.isnull(grades)
print("Missing Values:",null)

default_score=df.fillna(0)
print("Default Scores:",default_score)

mask=default_score[default_score[0]>60]

print("Filter masked:",mask)