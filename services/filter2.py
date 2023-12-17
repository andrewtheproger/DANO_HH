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
    res = df.copy()

    res["age"] = res["year_of_birth"].apply(lambda x: 2023 - x)
    res['age_category'] = res["year_of_birth"].apply(
        lambda x: f"{str((2023 - x) // 10 * 10)}-{str((2023 - x) // 10 * 10 + 10)}")
    print(res.shape)
    res = res.dropna(how="any")
    res = res[res["expected_salary"] > 0]
    if salary_lower_limit == "z":
        for i in list(set(list(res["profession"].values))):
            temp_res = res[res["profession"] == i]
            salary_lower_limit = max(temp_res["expected_salary"].mean() - 3 * temp_res["expected_salary"].std(), 0)
            if salary_lower_limit == 0:
                continue
            res["delete"] = res.apply(lambda x: int(x["profession"] == i and x["expected_salary"] < salary_lower_limit), axis=1)
            res = res[res["delete"] == 0]
            print(res.shape, salary_lower_limit)
    else:
        res = res[res["expected_salary"] > salary_lower_limit]
    if salary_upper_limit == "z":
        for i in list(set(list(res["profession"].values))):
            temp_res = res[res["profession"] == i]
            salary_upper_limit = temp_res["expected_salary"].mean() + 3 * temp_res["expected_salary"].std()
            res["delete"] = res.apply(lambda x: int(x["profession"] == i and x["expected_salary"] > salary_upper_limit), axis=1)
            res = res[res["delete"] == 0]
            print(res.shape, salary_upper_limit)
    else:
        res = res[res["expected_salary"] < salary_upper_limit]
    res = res[(res["work_experience_months"] + 168) / 12 < 2023 - res["year_of_birth"]]
    res = res[res["year_of_birth"] < birth_min]
    res = res[res["year_of_birth"] > birth_max]
    res = res[res["work_experience_months"] >= required_exp]
    del res["delete"]
    res["delete_pensioner"] = res.apply(lambda x: int((x["gender"] == "male" and x["age"] >= 58) or (x["gender"] == "female" and x["age"] >= 63)), axis=1)
    res = res[res["delete_pensioner"] == 0]
    del res["delete_pensioner"]
    if higher_required:
        res = res[res["education_level"].isin(["higher", "bachelor", "master", "candidate", "doctor"])]
    if only_final_invitation:
        res = res[res["final_state"] == "invitation"]
    if only_initial_response:
        res = res[res["initial_state"] == "response"]
    print(res.shape)

    return res
