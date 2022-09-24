import numpy as np
import pandas
import pandas as pd
from pandas_profiling import ProfileReport

dataset_1 = pd.read_csv("../dataset1.csv")
# profile_1 = ProfileReport(dataset_1, title="dataset1")
# profile_1.to_file("dataset1_profiling_result")

dataset_2 = pd.read_csv("../dataset2.csv")
# profile_2 = ProfileReport(dataset_2, title="dataset2")
# profile_2.to_file("dataset2_profiling_result")

# Find out the dot
dataset_1_with_dot = dataset_1[dataset_1["name"].str.contains(".", regex=False)]
print(dataset_1_with_dot)

# Extract the dot and distinct
dataset_1_extract_with_dot_distinct = dataset_1_with_dot["name"].str.split(" ")
pandas.set_option("display.max_rows", 200)
print(dataset_1_extract_with_dot_distinct.drop_duplicates())

# Appears dot can also exist in the last word such as Jr.
#  Last with dot is trivial since requirement does not need it anyway
