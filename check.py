import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from services.filter import filter_dataset
from services.get_group import age_grouping
df = pd.read_csv('hh_ru_dataset.csv', sep=',')
fig, ax = plt.subplots(figsize=(5, 5))
fig = sns.boxplot(x="expected_salary", data=df)
fig = ax.get_figure()
plt.ylabel('Количество людей')
plt.xlabel("Возраст")
plt.suptitle('Распределение возрастов')
fig.savefig("возрастов" + '.png', transparent=True)