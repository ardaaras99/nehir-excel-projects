from project1.utils import check_reached_certain_amount, read_excel

results_df = read_excel(path="data/Startups Flanders 2020.xlsx", sheet_name="Results")
target_col = "Reached 1M Added value 1 YES 0 NO"

look_cols = [
    "Added value 2023",
    "Added value2022",
    "Added value 2021",
    "Added value 2020",
    "Added value 2019",
    "Added value 2018",
    "Added value 2017",
    "Added value 2016",
]


result_df = check_reached_certain_amount(
    results_df, target_col, look_cols, certain_amount=1_000
)
output_path = "output/2020/Startups Flanders 2020 Arda.xlsx"
results_df.to_excel(output_path, sheet_name="Results", index=False)
