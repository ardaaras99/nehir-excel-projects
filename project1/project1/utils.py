from pathlib import Path

import pandas as pd


def read_excel(path: Path, sheet_name: str) -> pd.DataFrame:
    return pd.read_excel(path, sheet_name=sheet_name)


def check_reached_certain_amount(
    results_df: pd.DataFrame, target_col: str, look_cols: list[str], certain_amount: int
):
    for index, row in results_df.iterrows():
        for column in look_cols:
            value = row[column]
            if value == "n.a.":
                value = 0
            else:
                value = float(str(value).replace(",", "."))
            if value >= certain_amount:
                results_df.at[index, target_col] = 1
                break
    return results_df
