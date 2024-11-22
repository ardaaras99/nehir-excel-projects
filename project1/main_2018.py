import pandas as pd

from project1.utils import check_reached_certain_amount

results_df = pd.read_excel(
    "data/Startups Flanders 2018.xlsx",
    sheet_name="Results",
    parse_dates=["Date of incorporation"],
)
target_col = "Reached 5M added value 1 YES 0 NO"


# Define the columns to look at
look_cols = [
    "Added value 2023",
    "Added value 2022",
    "Added value 2021",
    "Added value 2020",
    "Added value 2019",
    "Added value 2018",
    "Added value 2017",
    "Added value 2016",
    "Added value 2015",
    "Added value 2014",
]

results_df = check_reached_certain_amount(
    results_df, target_col, look_cols, certain_amount=5_000
)


def calculate_years_to_reach_value(df, look_cols, target_value, column_name):
    year_of_inc = df["Date of incorporation"].dt.year
    df[column_name] = None

    for index, row in df.iterrows():
        years_to_reach_value = None
        for column in reversed(look_cols):
            value = row[column]
            if value == "n.a.":
                value = 0
            else:
                value = float(str(value).replace(",", "."))
            if value >= target_value:
                year = int(column.split()[-1])  # Extract the year from the column name
                years_to_reach_value = year - year_of_inc[index]
                break
        df.at[index, column_name] = years_to_reach_value


# Calculate the number of years required to reach 1M added value
calculate_years_to_reach_value(
    results_df, look_cols, 1_000, "Number of years required to reach 1M Added value"
)

# Calculate the number of years required to reach 5M added value
calculate_years_to_reach_value(
    results_df, look_cols, 5_000, "Number of years required to reach 5M Added value"
)

# Save the updated DataFrame back to Excel
output_path = "output/2018/Startups Flanders 2018 Arda.xlsx"
results_df.to_excel(output_path, sheet_name="Results", index=False, engine="openpyxl")
