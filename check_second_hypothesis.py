import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ks_2samp, shapiro, mannwhitneyu, kendalltau
from filter import filter_dataset
from correlation_categorical_numerical import correlation_categorical_numerical
from correlation_categorical_categorical import correlation_categorical_categorical


def main(name):
    df = pd.read_csv(name, sep=',', skipinitialspace=True)
    df = filter_dataset(df, higher_required=True, required_exp=120, salary_lower_limit=0, only_initial_response=True)
    resume_ids = df["resume_id"].value_counts().rename_axis('resume').to_frame('counts')
    df["count_responses"] = df.apply(lambda x: resume_ids.loc[x["resume_id"]]["counts"], axis=1)
    print(df["count_responses"])
    resume_ids2 = df["resume_id"].value_counts()
    resume_ids2 = resume_ids2[resume_ids2 > 1]
    resume_ids2 = list(pd.Series(resume_ids2.keys()))
    df["is_multiple"] = df.apply(lambda x: x["resume_id"] in resume_ids2, axis=1)
    print(df["count_responses"].head(10))
    for column in ["expected_salary", "compensation_from", "compensation_to", "year_of_birth", "work_experience_months"]:
        print(f'Корреляция {column} с тем, прошел человек одно собеседование или несколько: ',
              correlation_categorical_numerical(df["is_multiple"], df[column]))
        print("p-value для этого вывода:", mannwhitneyu(df[df["is_multiple"] == 0][column],
                                                        df[df["is_multiple"] == 1][column])[1])
        fig, ax = plt.subplots()
        fig = sns.histplot(x=column, data=filter_dataset(df, salary_lower_limit=150000), hue="is_multiple", bins=20, stat='density', common_norm=False, kde=True)
        fig = ax.get_figure()
        fig.savefig("charts/" + column + "_check_multiple" + '.png')
    print(df.shape)
    df = filter_dataset(df, salary_lower_limit=150000)
    print(df.shape)
    print()
    print(df.corr(method="spearman")["count_responses"]["work_experience_months"])
    print()
    print(df[df["is_multiple"] == 0]["profession"].value_counts(normalize=True))
    print(df[df["is_multiple"] == 1]["profession"].value_counts(normalize=True))
    print(correlation_categorical_numerical(df[df["is_multiple"] == 1]["final_state"],
                                            df[df["is_multiple"] == 1]["expected_salary"]))
    print(correlation_categorical_numerical(df["final_state"],
                                            df["expected_salary"]))


main("hh_ru_dataset.csv")