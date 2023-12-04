import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def data_prep(name):
    df = pd.read_csv(name, sep=',', skipinitialspace=True)
    df.dropna(how="any")
    df1 = df[df["initial_state"] == "response"]
    print(df1["final_state"].value_counts())
    df2 = df[df["initial_state"] == "invitation"]
    print(df2["final_state"].value_counts())
    df3 = df[df["initial_state"] == "discard"]
    print(df3["final_state"].value_counts())
    df = df[(df["final_state"] == "invitation")]
    df = df[df["work_schedule"] == "full_day"]
    df = df[df["year_of_birth"] > 1922]
    df = df[df["work_experience_months"] < 1000]
    upper_limits = dict()
    for i in list(set(df["profession"].values)):
        df_temp = df[df["profession"] == i]
        q3, q1 = np.nanpercentile(df_temp["expected_salary"], [75, 25])
        iqr = q3 - q1
        upper_limits[i] = q3 + 3 * iqr
    df = df[df["expected_salary"] < 1000000]
    df = df[df["compensation_from"] > 0]
    fig, ax = plt.subplots()
    fig = sns.scatterplot(x="compensation_from", y="compensation_to", data=df)
    fig = ax.get_figure()
    fig.savefig('scatter.png')
    df_temp = df.copy()
    for i in [12, 24, 36, 48, 60, 72]:
        df_temp = df[df["work_experience_months"] <= i]
        df["gap"] = df.apply(lambda x: x["expected_salary"] / x["compensation_from"], axis=1)
        df["gap"] = df["gap"].astype(float)
        print(df_temp.corr(method="kendall", numeric_only=True).head(5))


data_prep("hh_ru_dataset.csv")