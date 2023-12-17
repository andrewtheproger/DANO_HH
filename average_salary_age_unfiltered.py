import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from services.filter import filter_dataset
from services.get_group_2 import age_grouping
from services.get_resume_df import get_resumes
df = pd.read_csv('hh_ru_dataset.csv', sep=',')
fig, ax = plt.subplots(figsize=(8, 8))
df["age"] = df["year_of_birth"].apply(lambda x: 2023 - x)
df['age_category'] = df["year_of_birth"].apply(
    lambda x: f"{str((2023 - x) // 10 * 10)}-{str((2023 - x) // 10 * 10 + 10)}")
df["start"] = df["age"] - df["work_experience_months"] / 12
print(df[df["gender"] == "male"]["start"].mean())
print(df[df["gender"] == "female"]["start"].mean())
df = df.sort_values('age').reset_index()
fig = sns.barplot(color="#FFF465", x="age_category", y="expected_salary", data=df)
fig = ax.get_figure()
plt.rc('xtick', labelsize=10 )
plt.rc('ytick', labelsize=10 )
plt.suptitle('')
plt.ylabel("")
plt.xlabel("")
fig.savefig("charts_final/Средняя зарплата по возрасту без фильтра" + '.png', transparent=True)