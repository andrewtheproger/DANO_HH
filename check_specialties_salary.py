import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from services.filter import filter_dataset
from services.get_group import age_grouping
df = pd.read_csv('hh_ru_dataset.csv', sep=',')
from services.get_resume_df import get_resumes
df = filter_dataset(df)
fig, ax = plt.subplots(figsize=(12, 6))
fig = sns.barplot(color="#FFF465", x="year_of_birth", data=df[df["profession"] == "Программист, разработчик"], palette=sns.color_palette(["#FFF465", "#FFF465", "#FFF465", "#FFF465", "#FFF465", "#FFF465"]))
fig = ax.get_figure()
plt.ylabel('')
plt.xlabel("")
fig.savefig("charts_final/Распределение возрастов фильтр" + '.png', transparent=True)