import pandas as pd

data = pd.read_excel("D:\Youtube\lln_excel_subs_2025-4-26_7332586.xlsx")

subtitle = data["Subtitle"]
time = data["Time"]

print(subtitle)
print(time)