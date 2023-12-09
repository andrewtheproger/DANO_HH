import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from filter import filter_dataset
df = pd.read_csv('hh_ru_dataset.csv', sep=',')
df = filter_dataset(df, salary_upper_limit=500000, only_final_invitation=True, only_initial_response=True)
df["age"] = df["year_of_birth"].apply(lambda x: 2023 - x)
df['age_category'] = df["year_of_birth"].apply(
    lambda x: f"{str((2023 - x) // 10 * 10)}-{str((2023 - x) // 10 * 10 + 10)}")
df = df[df["final_state"] == "invitation"]
professions = list(set(list(df["profession"].values)))
gender = "male"
for profession in professions:
    fig, ax = plt.subplots(figsize=(10, 10))
    temp_df = df[(df["profession"] == profession) & (df["gender"] == gender)]
    temp_df = temp_df.sort_values('age').reset_index()
    fig = sns.barplot(y="expected_salary", x="age_category", data=temp_df)
    fig = ax.get_figure()
    if profession == "Менеджер/руководитель АХО":
        profession = "Менеджер АХО"
    plt.ylabel('Зарплата, руб.')
    plt.xlabel('Возрастная категория')
    correlation = temp_df.corr(numeric_only=True)["expected_salary"]["year_of_birth"]
    plt.suptitle(f'Средняя зарплата для специалистов "{profession}"')

    fig.savefig("charts/Профессии_средняя_зарплата_по_возрасту/" + profession + "_" + "мужчины" + '.png')
gender = "female"
for profession in professions:
    fig, ax = plt.subplots(figsize=(10, 10))
    temp_df = df[(df["profession"] == profession) & (df["gender"] == gender)]
    temp_df = temp_df.sort_values('age').reset_index()
    fig = sns.barplot(y="expected_salary", x="age_category", data=temp_df)
    fig = ax.get_figure()
    if profession == "Менеджер/руководитель АХО":
        profession = "Менеджер АХО"
    plt.ylabel('Зарплата, руб.')
    plt.xlabel('Возрастная категория')
    correlation = temp_df.corr(numeric_only=True)["expected_salary"]["year_of_birth"]
    plt.suptitle(f'Средняя зарплата для специалистов "{profession}"')

    fig.savefig("charts/Профессии_средняя_зарплата_по_возрасту/" + profession + "_" + "женщины" + '.png')