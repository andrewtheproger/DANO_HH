import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from filter import filter_dataset
from get_group import age_grouping
from scipy.stats import mannwhitneyu


df = pd.read_csv('hh_ru_dataset.csv', sep=',')
df = filter_dataset(df, salary_upper_limit=500000, only_final_invitation=True, only_initial_response=True)
df["age"] = df["year_of_birth"].apply(lambda x: 2023 - x)
df['age_category'] = df["year_of_birth"].apply(
    lambda x: f"{str((2023 - x) // 10 * 10)}-{str((2023 - x) // 10 * 10 + 10)}")
df = df[df["final_state"] == "invitation"]
professions = list(set(list(df["profession"].values)))
df = age_grouping(df)
for profession in professions:
    fig, ax = plt.subplots(figsize=(10, 10))
    temp_df = df[(df["profession"] == profession) & (df["young"] == 0)]
    temp_df = temp_df.sort_values('age').reset_index()
    p = mannwhitneyu(temp_df[temp_df["elderly"] == 1]['expected_salary'],
                     temp_df[temp_df["middle_aged"] == 1]['expected_salary'])[1]
    fig = sns.barplot(y="expected_salary", x="elderly", data=temp_df)
    fig = ax.get_figure()
    if profession == "Менеджер/руководитель АХО":
        profession = "Менеджер АХО"
    plt.ylabel('Зарплата, руб.')
    plt.suptitle(f'{str(round(p, 3))} "{profession}"')

    fig.savefig("charts/Профессии_среднее_по_двум_группам/" + profession + "_" + "женщины" + '.png')