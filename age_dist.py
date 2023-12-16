import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from services.filter import filter_dataset
from services.get_group import age_grouping
df = pd.read_csv('hh_ru_dataset.csv', sep=',')
from services.get_resume_df import get_resumes
df["age"] = df["year_of_birth"].apply(lambda x: 2023 - x)
df['age_category'] = df["year_of_birth"].apply(
    lambda x: f"{str((2023 - x) // 10 * 10)}-{str((2023 - x) // 10 * 10 + 10)}")
df = age_grouping(df)
df = get_resumes(df)
df = filter_dataset(df,  only_initial_response=False, only_final_invitation=False, salary_upper_limit=5 * 10 ** 7)
fig, ax = plt.subplots(figsize=(6, 6))
fig = sns.histplot(color="#FFF465", bins=72, kde=True, x="age", data=df, palette=sns.color_palette(["#FFF465", "#FFF465", "#FFF465", "#FFF465", "#FFF465", "#FFF465"]))
fig = ax.get_figure()
plt.ylabel('')
plt.xlabel("")
fig.savefig("charts_final/Распределение возрастов" + '.png', transparent=True)