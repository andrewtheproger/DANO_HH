import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from filter import filter_dataset
from get_group import age_grouping
from scipy.stats import mannwhitneyu
from specialty_grouping import distribute_professions


plt.style.use("dark_background")
df = pd.read_csv('hh_ru_dataset.csv', sep=',')
df = filter_dataset(df, salary_upper_limit=500000, only_final_invitation=False, only_initial_response=True)
df["age"] = df["year_of_birth"].apply(lambda x: 2023 - x)
df['age_category'] = df["year_of_birth"].apply(
    lambda x: f"{str((2023 - x) // 10 * 10)}-{str((2023 - x) // 10 * 10 + 10)}")
print(distribute_professions(df))
specialties = list(set(list(df["specialty"].values)))
df = age_grouping(df)
for specialty in specialties:
    fig, ax = plt.subplots(figsize=(10, 10))
    temp_df = df[(df["specialty"] == specialty) & (df["young"] == 0)]
    temp_df = temp_df.sort_values('age').reset_index()
    p = mannwhitneyu(temp_df[temp_df["elderly"] == 1]['expected_salary'],
                     temp_df[temp_df["middle_aged"] == 1]['expected_salary'])[1]
    fig = sns.barplot(y="expected_salary", x="elderly", data=temp_df, palette="rocket")
    fig = ax.get_figure()
    if specialty == "Менеджер/руководитель АХО":
        specialty = "Менеджер АХО"
    plt.ylabel('Зарплата, руб.')
    plt.suptitle(f'{str(round(p, 3))} "{specialty}"')

    fig.savefig("charts/Зарплата_по_специализациям/" + specialty + '.png')