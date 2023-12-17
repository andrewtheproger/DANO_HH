import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from services.filter import filter_dataset
from services.get_group_2 import age_grouping
from services.get_resume_df import get_resumes
df = pd.read_csv('hh_ru_dataset.csv', sep=',')
df = filter_dataset(df,  only_initial_response=False, only_final_invitation=False, salary_upper_limit=5 * 10 ** 7)
fig, ax = plt.subplots(figsize=(8, 8))
df = df.sort_values('age').reset_index()
fig = sns.barplot(color="#FFF465", x="age_category", y="expected_salary", data=df)
fig = ax.get_figure()
plt.rc('xtick', labelsize=10 )
plt.rc('ytick', labelsize=10 )
plt.suptitle('')
plt.ylabel("")
plt.xlabel("")
fig.savefig("charts_final/Средняя зарплата по возрасту" + '.png', transparent=True)