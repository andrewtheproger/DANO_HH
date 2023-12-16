from services.get_group_2 import age_grouping
from services.get_resume_df import get_resumes


def filter_dataset(df,
                   higher_required=False,
                   salary_upper_limit="z",
                   salary_lower_limit="z",
                   only_initial_response=False,
                   only_final_invitation=False,
                   required_exp=0,
                   birth_max=1922,
                   birth_min=2023):

    if salary_lower_limit == "z":
        salary_lower_limit = max(df["expected_salary"].mean() - 3 * df["expected_salary"].std(), 0)
    if salary_upper_limit == "z":
        salary_upper_limit = df["expected_salary"].mean() + 3 * df["expected_salary"].std()
    res = df.copy()
    res = res[res["work_schedule"] == "full_day"]
    print(res.shape)
    res = res.dropna(how="any")
    print(res.shape)
    res = res[(res["work_experience_months"] + 168) / 12 < 2023 - res["year_of_birth"]]
    print(res.shape)
    res = res[res["year_of_birth"] < birth_min]
    print(res.shape)
    res = res[res["year_of_birth"] > birth_max]
    print(res.shape)
    res = res[res["expected_salary"] > salary_lower_limit]
    print(res.shape)
    res = res[res["expected_salary"] < salary_upper_limit]
    print(res.shape)
    res = res[res["work_experience_months"] >= required_exp]
    print(res.shape)
    work_experience_months_upper_limit = df["work_experience_months"].mean() + 4.5 * df["work_experience_months"].std()
    res = res[res["work_experience_months"] <= work_experience_months_upper_limit]
    print(res.shape)
    res = get_resumes(res)
    print(res.shape)
    res["delete_pensioner"] = res.apply(lambda x: int((x["gender"] == "male" and x["age"] >= 58) or (x["gender"] == "female" and x["age"] >= 63)), axis=1)
    print(res.shape)
    res = res[res["delete_pensioner"] == 0]
    print(res.shape)
    del res["delete_pensioner"]
    print(res.shape)
    if higher_required:
        res = res[res["education_level"].isin(["higher", "bachelor", "master", "candidate", "doctor"])]
    if only_final_invitation:
        res = res[res["final_state"] == "invitation"]
    if only_initial_response:
        res = res[res["initial_state"] == "response"]
    print(res)
    return res
