#!/usr/bin/env python3

from os import sep
import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df.replace({"Re": np.nan, "New": None}, inplace=True)
    df.dropna(inplace=True)

    return df[df["Pos"] > df["LW"].map(int)]

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
