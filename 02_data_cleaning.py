import pandas as pd
df=pd.read_csv("data/LC_loans_granting_model_dataset.csv")
# print(df.shape)
# print(df.isnull().sum())
# print(df["dti_n"].describe())
# print(df["revenue"].describe())
# print(df["fico_n"].describe())
# print(df["loan_amnt"].describe())
# print(df["experience_c"].value_counts())
# print(df["Default"].value_counts())
# print(df["id"].duplicated().sum())
# print((df["loan_amnt"]<0).sum())
# print((df["revenue"]<0).sum())
# print((df["dti_n"]<0).sum())
df["issue_d"] = pd.to_datetime(
    df["issue_d"],
    format="%b-%Y"
)
# print(df["issue_d"].head())
# print(df["issue_d"].min()), "to",print(df["issue_d"].max())

# print((df["dti_n"]==999).sum())
# print(df.loc[df["dti_n"]==999,"Default"].mean()*100)
# print(df["revenue"].nlargest(10).tolist())
# print(
#     df.nlargest(10, "revenue")[
#         ["id", "revenue", "loan_amnt", "fico_n", "dti_n", "Default"]
#     ]
# )
# print(df["revenue"].quantile([0.90,0.95,0.99,0.999]))

# df["revenue_ratio"]=df["revenue"]/df["loan_amnt"]
# print(df["revenue_ratio"].describe())
# print(
#     df.nlargest(10, "revenue_ratio")[
#         ["id", "revenue", "loan_amnt", "revenue_ratio", "Default"]
#     ]
# )
# print(df[["revenue","loan_amnt","fico_n","dti_n","Default"]].corr())

dti_999=df[df["dti_n"]==999]
# print(dti_999[
#     [
#         "id",
#         "loan_amnt",
#         "fico_n",
#         "dti_n",
#         "emp_length",
#         "purpose",
#         "home_ownership_n",
#         "Default"
#     ]
# ])
# print(len(dti_999))
# print(dti_999["Default"].value_counts())
# print(dti_999["Default"].mean()*100)

df["dti_n"]=df["dti_n"].replace(999,pd.NA)
# print(df["dti_n"].isna().sum())
# print(df.shape)

df=df.drop(columns=["desc"])
df=df.drop(columns=["title"])
df["zip_code"]=df["zip_code"].fillna("Unknown")
# print(df.isnull().sum())
# print(df.shape)

# print(df[["revenue","dti_n","loan_amnt","fico_n"]].describe())
# print((df["loan_amnt"]<=0).sum())
# print((df["revenue"]<=0).sum())
# print(((df["fico_n"]<300) | (df["fico_n"]>850)).sum())
# print((df["dti_n"]<0).sum())
# print(df["Default"].value_counts())

output_path="data/LC_loans_cleaned.csv"
df.to_csv(output_path,index=False)
print(output_path)
print(df.shape)