import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from services.filter import filter_dataset
from services.filter2 import filter_dataset as f
from services.get_group_2 import age_grouping
from services.get_resume_df import get_resumes
from services.correlation_categorical_categorical import correlation_categorical_categorical
from services.correlation_categorical_numerical import correlation_categorical_numerical
df = pd.read_csv('hh_ru_dataset.csv', sep=',')
df_reserve = df.copy()
df1 = filter_dataset(df, required_exp=5)
df = filter_dataset(df)
print(df["relocation_status"].value_counts())
print(df["business_trip_readiness"].value_counts())
average = {}
for profession in list(set(list(df1["profession"].values))):
    average[profession] = df1[df1["profession"] == profession]["expected_salary"].mean()
print(average)
df["undervalue"] = df.apply(lambda x: x["expected_salary"] / average[x["profession"]], axis=1)
print(df["undervalue"].value_counts())
df["was_employed"] = df["resume_id"].isin(list(set(list(df_reserve[df_reserve["final_state"] == "invitation"]["resume_id"]))))
print(df["was_employed"].value_counts())
df = df[df["work_experience_months"] == 0]
print(correlation_categorical_categorical(df["was_employed"], df["education_level"]))
