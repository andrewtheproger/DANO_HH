import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from services.filter import filter_dataset
from services.correlation_categorical_numerical import correlation_categorical_numerical

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
new_values = {
    "female": 0,
    "male": 1
}
plt.style.use("dark_background")


def main(name):
    df = pd.read_csv(name, sep=',', skipinitialspace=True)
    df = filter_dataset(df,
                        higher_required=False,
                        required_exp=120,
                        salary_lower_limit=0,
                        salary_upper_limit=1000000,
                        only_initial_response=True,
                        birth_max=1922,
                        birth_min=1970)
    counts = df['resume_id'].value_counts()
    df['freq'] = df['resume_id'].map(counts)
    df = filter_dataset(df, only_final_invitation=True)
    print(pd.DataFrame(df.corr(method="spearman", numeric_only=True)))
    print(pd.DataFrame(filter_dataset(df, higher_required=True).corr(method="spearman", numeric_only=True)))
    df["gender"] = df["gender"].apply(lambda x: new_values[x])
    for column in ["expected_salary", "compensation_from", "compensation_to", "year_of_birth",
                   "work_experience_months", 'freq']:
        fig, ax = plt.subplots()
        fig = sns.histplot(x=column, data=df, bins=20, stat='density', common_norm=False, kde=True, palette="rocket")
        fig = ax.get_figure()
        fig.savefig("charts/" + column + "_check_elderly" + '.png')
        print(column, correlation_categorical_numerical(df["gender"], df[column]))


main("hh_ru_dataset.csv")