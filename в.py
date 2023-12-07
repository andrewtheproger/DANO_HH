import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('hh_ru_dataset.csv', sep=',')
df = df[df["profession"] == "Юрист"]
counts = df['resume_id'].value_counts()
df['Частота'] = df['resume_id'].map(counts)
df['exp_category'] = df["work_experience_months"].apply(lambda x: x // 36)
df = df[df["final_state"] == "invitation"]
fig, ax = plt.subplots()
fig = sns.barplot(y="Частота", x="exp_category", data=df)
fig = ax.get_figure()
fig.savefig('b.png')