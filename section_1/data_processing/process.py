import os
import pathlib
import glob

import numpy as np
import pandas as pd
import argparse

from pandas import DataFrame


def main():
    OUTPUT_SCHEMA = ["first_name", "last_name", "price", "above_100"]

    # parse args
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    args = parser.parse_args()

    # resolve directory
    current_directory = pathlib.Path(__file__)
    csv_source_directory = current_directory.parent.parent.resolve() / "source"
    csv_sink_directory = current_directory.parent.parent.resolve() / "sink"
    csv_source_file_path = csv_source_directory / args.date
    csv_sink_file_path = csv_sink_directory / args.date

    # read the file in as df
    df = read_source(csv_source_file_path)

    # filter rows with empty name
    remove_empty_name(df)

    # split name into first_name and last_name
    spilt_name(df)

    # ensure schema
    df = ensure_schema(df)

    # check if price > 100
    is_above_100(df)

    df = df[OUTPUT_SCHEMA]
    write_sink(df, csv_sink_file_path)


def read_source(path) -> DataFrame:
    csv_files = glob.glob(str(path / "*.csv"))
    df = []
    for f in csv_files:
        csv = pd.read_csv(f)
        df.append(csv)
    return pd.concat(df)


def remove_empty_name(df: DataFrame) -> None:
    df["name"].replace("", np.nan, inplace=True)
    df.dropna(subset=["name"], inplace=True)


def spilt_name(df: DataFrame) -> None:
    df["name"].replace(r"[a-zA-Z]+\. ", "", regex=True, inplace=True)
    names = df["name"].str.split(" ", expand=True)
    df[["first_name", "last_name"]] = names.get([0, 1])
    df.drop(columns=["name"], inplace=True)


def ensure_schema(df: DataFrame) -> DataFrame:
    return df.astype({
        "first_name": "object",
        "last_name": "object",
        "price": "float64",
    })


def is_above_100(df: DataFrame) -> None:
    df["above_100"] = df["price"] > 100.0


def write_sink(df, path) -> None:
    if not os.path.exists(path):
        os.mkdir(path)
    df.to_csv(str(path / "result.csv"), index=False)


if __name__ == "__main__":
    main()
