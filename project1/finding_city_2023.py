import pandas as pd

results_df = pd.read_excel(
    "data/Startups Flanders 2023- new.xlsx",
    sheet_name="Results",
    parse_dates=["Date of incorporation"],
)

column_name = "City"

# find the statistics of the column

print(results_df[column_name].value_counts())

output = results_df[column_name].value_counts().to_frame()
output.columns = ["Count"]
output.index.name = column_name
output = output.reset_index()
output.to_excel("output/city_statistics.xlsx", index=False)
