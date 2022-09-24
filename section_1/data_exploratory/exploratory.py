import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

dataset_1 = pd.read_csv("../dataset1.csv")
profile_1 = ProfileReport(dataset_1, title="dataset1")
profile_1.to_file("dataset1_profiling_result")

dataset_2 = pd.read_csv("../dataset2.csv")
profile_2 = ProfileReport(dataset_2, title="dataset2")
profile_2.to_file("dataset2_profiling_result")

