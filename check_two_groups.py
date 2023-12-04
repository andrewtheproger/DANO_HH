import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ks_2samp, shapiro, mannwhitneyu, kendalltau
from filter import filter_dataset
from correlation_categorical_numerical import correlation_categorical_numerical


def main(name):
    df = pd.read_csv(name, sep=',', skipinitialspace=True)
    df = filter_dataset(df, higher_required=True, required_exp=120, salary_lower_limit=150000, only_initial_response=True, only_final_invitation=False)
    resume_ids = df["resume_id"].value_counts()
    resume_ids = resume_ids[resume_ids > 1]
    resume_ids = list(pd.Series(resume_ids.keys()))
    df["is_multiple"] = df.apply(lambda x: x["resume_id"] in resume_ids, axis=1)
    for column in ["expected_salary", "compensation_from", "compensation_to", "year_of_birth", "work_experience_months"]:
        print(column, correlation_categorical_numerical(df["is_multiple"], df[column]))
        print(mannwhitneyu(df[df["is_multiple"] == 0][column], df[df["is_multiple"] == 1][column]))
        fig, ax = plt.subplots()
        fig = sns.histplot(x=column, data=df, hue="is_multiple", bins=20, stat='density', common_norm=False, kde=True)
        fig = ax.get_figure()
        fig.savefig("charts/" + column + "_check_multiple" + '.png')
    print(df.shape)
    print(df[df["is_multiple"] == 0]["profession"].value_counts(normalize=True))
    print(df[df["is_multiple"] == 1]["profession"].value_counts(normalize=True))
    print(correlation_categorical_numerical(df[df["is_multiple"] == 1]["final_state"], df[df["is_multiple"] == 1]["expected_salary"]))


main("hh_ru_dataset.csv")