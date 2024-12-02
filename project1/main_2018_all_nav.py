# %%
import pandas as pd

df = pd.read_excel("data/2018 ALL NAV.xlsx")

# First check the date of incorporation year to find the year we need to start
start_year = df["Date of incorporation"].dt.year
look_cols = [f"Net added value\nth EUR\n{x}" for x in range(2015, 2024)]


def years_to_reach_value(df, look_cols, start_year, target_value, target_value_str):
    for index, row in df.iterrows():
        years_to_reach_value = None
        for column in look_cols:
            value = row[column]
            if value == "n.a.":
                value = 0
            if value >= target_value:
                year = int(column.split()[-1])
                years_to_reach_value = year - start_year[index]
                break
            else:
                years_to_reach_value = "Not Reached"
        fill_column = (
            f"number of years required \nto reach {target_value_str}M added value"
        )
        df.at[index, fill_column] = years_to_reach_value


target_value = 1_000
target_value_str = "1"
years_to_reach_value(df, look_cols, start_year, target_value, target_value_str)

target_value = 5_000
target_value_str = "5"
years_to_reach_value(df, look_cols, start_year, target_value, target_value_str)


# Set this column to 0 if the value is not reached and 1 if it is reached by looking at the years_to_reach_value column
df["reached 5M added value by 2023 \n1 YES"] = df[
    "number of years required \nto reach 5M added value"
].apply(lambda x: 1 if x != "Not Reached" else 0)
# %%
# Save the updated DataFrame back to Excel using openpyxl engine
output_path = "data/2018 ALL NAV ARDA.xlsx"
df.to_excel(output_path, index=False, engine="openpyxl")
# %%
