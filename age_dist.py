import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from services.filter import filter_dataset
from services.get_group import age_grouping
df = pd.read_csv('hh_ru_dataset.csv', sep=',')
from services.get_resume_df import get_resumes
df = get_resumes(df)
df = filter_dataset(df,  only_initial_response=False, only_final_invitation=False, salary_upper_limit=5 * 10 ** 7)
fig, ax = plt.subplots(figsize=(6, 6))
fig = sns.kdeplot(color="#FFF465", fill=True, x="age", data=df, palette=sns.color_palette(["#FFF465", "#FFF465", "#FFF465", "#FFF465", "#FFF465", "#FFF465"]))
fig = ax.get_figure()
plt.ylabel('')
plt.xlabel("")
fig.savefig("charts_final/Распределение возрастов" + '.png', transparent=True)