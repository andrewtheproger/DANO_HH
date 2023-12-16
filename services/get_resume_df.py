import pandas as pd


def get_resumes(df):
    return df.drop_duplicates(subset=["resume_id"])