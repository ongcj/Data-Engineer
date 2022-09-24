import pathlib

import numpy as np
import pandas as pd
import argparse

from pandas import DataFrame


def main():
    OUTPUT_SCHEMA = ["first_name", "last_name", "price", "above_100"]

    # parse args
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    # resolve directory
    current_directory = pathlib.Path(__file__)
    csv_source_directory = current_directory.parent.parent.resolve() / "source"
    csv_sink_directory = current_directory.parent.parent.resolve() / "sink"
    csv_source_file_path = csv_source_directory / args.file
    csv_sink_file_path = csv_sink_directory / f"result_{args.file}"

    # read the file in as df
    df = pd.read_csv(csv_source_file_path)

    # filter rows with empty name
    remove_empty_name(df)

    # split name into first_name and last_name
    spilt_name(df)

    # ensure schema
    df = ensure_schema(df)

    # check if price > 100
    is_above_100(df)

    df = df[OUTPUT_SCHEMA]
    df.to_csv(str(csv_sink_file_path), index=False)


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


if __name__ == "__main__":
    main()
