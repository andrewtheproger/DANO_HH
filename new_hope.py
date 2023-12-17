import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from services.filter2 import filter_dataset
from scipy.stats import pearsonr, kendalltau, spearmanr
from services.get_group_2 import age_grouping
from services.get_resume_df import get_resumes
from services.correlation_categorical_categorical import correlation_categorical_categorical
from services.correlation_categorical_numerical import correlation_categorical_numerical
df = pd.read_csv('hh_ru_dataset.csv', sep=',')
print(list(set(df["work_schedule.1"].values)))
df = filter_dataset(df, only_initial_response=True)
new_values1 = {
    "male": 0,
    "female": 1
}
new_values2 = {
    "invitation": 1,
    "discard": 0,
    "response": 0
}
new_values3 = {
    "full_day": 1,
    "flyInFlyOut": 2,
    "remote": 3,
    "shift": 4,
    "flexible": 5
}
df["gender"] = df["gender"].apply(lambda x: new_values1[x])
df["final_state"] = df["final_state"].apply(lambda x: new_values2[x])
df["work_schedule.1"] = df["work_schedule.1"].apply(lambda x: new_values3[x])
vacancy_ids = df["vacancy_id"].value_counts().rename_axis('vacancy').to_frame('counts')
df["count_responses"] = df.apply(lambda x: vacancy_ids.loc[x["vacancy_id"]]["counts"], axis=1)
print(df["count_responses"])
res = df.drop_duplicates(subset=["vacancy_id"])
vacancies = list(set(list(df[df["final_state"] == 1]["vacancy_id"].values)))
print(res["work_schedule.1"].value_counts())
res["was_closed"] = res['vacancy_id'].isin(vacancies)
print(res["was_closed"].value_counts())
print(res[res["compensation_to"] == "b41207109c4"])
res = res[res["compensation_from"] != 0]
print(res[res["compensation_from"] == "b41207109c4"])
res["gap"] = res.apply(lambda x: x["compensation_to"] / x["compensation_from"], axis=1)
print(res["gap"].value_counts())
print(correlation_categorical_categorical(res["profession"], res["higher"]))