def age_grouping(df):
    df["elderly"] = df.apply(lambda x: int((x["gender"] == "female" and 44 < x["age"] < 58) or
                                           (x["gender"] == "male" and 49 < x["age"] < 63)), axis=1)
    df["young"] = df.apply(lambda x: int((x["gender"] == "female" and x["age"] < 30) or
                                         (x["gender"] == "male" and x["age"] < 35)), axis=1)
    df["middle_aged"] = df.apply(lambda x: 1 - x["young"] - x["elderly"], axis=1)
    return df
