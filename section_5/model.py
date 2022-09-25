import pathlib

import pandas as pd
from pandas import DataFrame

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from sklearn.preprocessing import OrdinalEncoder


def load_data() -> DataFrame:
    # resolve directory
    current_directory = pathlib.Path(__file__)
    data_directory = current_directory.parent.resolve() / "data"
    data_file = "car.data"
    data_columns = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
    df = pd.read_csv(data_directory / data_file, header=None, names=data_columns)
    # buying is y
    # maint, doors, lug_boot, safety, class is x
    df.drop(columns=["persons"], inplace=True)
    return df


def explore_data(df: DataFrame) -> None:
    # summary of data
    df.info()
    print("\n\n")

    # x: maint, doors, lug_boot, safety, class is categorical
    # y: buying is categorical and well distributed
    for column in df.columns:
        print(df[column].value_counts())
        print("\n")


def prepare_data_for_training(df: DataFrame) -> (DataFrame, DataFrame,
                                                 DataFrame, DataFrame):
    x = df.drop(["buying"], axis=1)
    y = df["buying"]
    x_train, x_test, y_train, y_test = train_test_split(x,
                                                        y,
                                                        test_size=0.40,
                                                        random_state=42)

    # encode categorical with ordinal encoding
    maint_cost_category = ["low", "med", "high", "vhigh"]
    doors_category = ["2", "3", "4", "5more"]
    lug_boot_category = ["small", "med", "big"]
    safety_category = ["low", "med", "high"]
    class_category = ["unacc", "acc", "good", "vgood"]
    x_category = [ # maint, doors, lug_boot, safety, class
        maint_cost_category,
        doors_category,
        lug_boot_category,
        safety_category,
        class_category
    ]
    x_encoder = OrdinalEncoder(categories=x_category)
    x_train = x_encoder.fit_transform(x_train)
    x_test = x_encoder.fit_transform(x_test)
    return x_train, x_test, y_train, y_test


def fit_model(x_train, x_test, y_train, y_test):
    rf = RandomForestClassifier(max_depth=3, random_state=42, n_estimators=100)
    rf.fit(x_train, y_train)
    y_pred = rf.predict(x_test)
    return rf


if __name__ == "__main__":
    # resolve directory
    df = load_data()

    # explore data
    explore_data(df)

    # data preparation/pre-processing
    x_train, x_test, y_train, y_test = prepare_data_for_training(df)

    # build model
    model = fit_model(x_train, x_test, y_train, y_test)

    # predict
    x_value = [[2, 2, 2, 2, 2]]
    requirement = df = pd.DataFrame(x_value)

    result = model.predict(requirement)
    print(result)  # low
