def filter_dataset(df,
                   higher_required=False,
                   salary_upper_limit=10 ** 20,
                   salary_lower_limit=0,
                   only_initial_response=True,
                   only_final_invitation=True,
                   required_exp=0):
    res = df.copy()
    res = res.dropna(how="any")
    res = res[res["year_of_birth"] > 1922]
    res = res[res["expected_salary"] > salary_lower_limit]
    res = res[res["compensation_to"] > salary_lower_limit]
    res = res[res["compensation_from"] > salary_lower_limit]
    res = res[res["expected_salary"] < salary_upper_limit]
    res = res[res["compensation_to"] < salary_upper_limit]
    res = res[res["compensation_from"] < salary_upper_limit]
    res = res[res["work_schedule"] == "full_day"]
    res = res[res["work_experience_months"] >= required_exp]
    res = res[res["work_experience_months"] < 1000]
    if higher_required:
        res = res[res["education_level"].isin(["higher", "bachelor", "master", "candidate", "doctor"])]
    if only_final_invitation:
        res = res[res["final_state"] == "invitation"]
    if only_initial_response:
        res = res[res["initial_state"] == "response"]
    return res
