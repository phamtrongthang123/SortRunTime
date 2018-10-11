import pandas as pd

data1 = pd.read_csv("out_ngaunhien.csv", names=["Sort", "Time", "N"])
from pandas import ExcelWriter
writer = ExcelWriter('filename.xlsx')
data1.to_excel(writer,'Sheet1')
writer.save()