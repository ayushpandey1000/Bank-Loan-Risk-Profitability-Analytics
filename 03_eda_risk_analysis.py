import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("data/LC_loans_cleaned.csv")

# default_counts=df["Default"].value_counts()
# print("Default Distribution")
# print(default_counts)
# default_rate=df["Default"].mean()*100
# print("Overall Default rate:")
# print(f"{default_rate:.2f}%")
# labels=["Fully Paid","Default"]
# plt.bar(labels,default_counts.values)
# plt.title("Loan Default Distribution")
# plt.xlabel("Loan Status")
# plt.ylabel("Number Of loans")
# plt.tight_layout()
# plt.show()

# df["fico_band"]=pd.cut(df["fico_n"],bins=[0,650,700,750,850],labels=["Below 650","650-699","700-749","750+"])
# fico_default_rate=(
#     df.groupby("fico_band",observed=False)["Default"].mean()*100
# )
# print("Default rate by fico band:")
# print(fico_default_rate)
# fico_default_rate.plot(kind="bar")
# plt.title("Default rate by fico score")
# plt.xlabel("Fico Score Band")
# plt.ylabel("Default rate (%)")
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.show()

# df["dti_band"]=pd.cut(
#     df["dti_n"],
#     bins=[-1,10,20,30,40,1000],labels=["0-10","10-20","20-30","30-40","40+"]
# )
# dti_default_rate=(
#     df.groupby("dti_band",observed=False)["Default"].mean()*100
# )
# print("Default rate by dti band:")
# print(dti_default_rate)
# dti_default_rate.plot(kind="bar")
# plt.title("Default rate by dti band")
# plt.xlabel("Dti band")
# plt.ylabel("Default rate (%)")
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.show()

# df["loan_band"]=pd.cut(
#     df["loan_amnt"],bins=[0,5000,10000,20000,30000,40000],
#     labels=["0-5k","5k-10k","10k-20k","20k-30k","30k-40k"]
# )
# laon_default_rate=(
#     df.groupby("loan_band",observed=False)["Default"].mean()*100
#     )
# print("Default rate by loan_amnt band:")
# print(laon_default_rate)
# laon_default_rate.plot(kind="bar")
# plt.title("Default rate by loan amnt")
# plt.xlabel("Loan amount band")
# plt.ylabel("Default rate (%)")
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.show()

# df["income_band"] = pd.cut(
#     df["revenue"],
#     bins=[0, 40000, 60000, 90000, 150000, float("inf")],
#     labels=["Below 40K", "40K-60K", "60K-90K", "90K-150K", "150K+"]
# )
# income_default_rate = (
#     df.groupby("income_band", observed=False)["Default"].mean() * 100
# )
# print("\nDefault Rate by Income Band:")
# print(income_default_rate)
# income_default_rate.plot(kind="bar")
# plt.title("Default Rate by Annual Income")
# plt.xlabel("Annual Income Band")
# plt.ylabel("Default Rate (%)")
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.show()

# purpose_default_rate=(
#     df.groupby("purpose")["Default"].mean().sort_values(ascending=False)*100
# )
# print("Default rate by loan purpose:")
# print(purpose_default_rate)
# purpose_default_rate.plot(kind="bar")
# plt.title("Default rate by loan purpose")
# plt.xlabel("Default rate*(%)")
# plt.ylabel("Loan Purpose")
# plt.tight_layout()
# plt.show()

# employment_default_rate = (
#     df.groupby("emp_length")["Default"].mean().sort_values(ascending=False) * 100
# )
# print("\nDefault Rate by Employment Length:")
# print(employment_default_rate)
# employment_default_rate.plot(kind="bar")
# plt.title("Default Rate by Employment Length")
# plt.xlabel("Employment Length")
# plt.ylabel("Default Rate (%)")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# state_default_rate=(
#     df.groupby("addr_state")["Default"].mean().sort_values(ascending=False)*100
# )
# print("Default rate by state")
# print(state_default_rate)
# top_states=state_default_rate.head(15)
# top_states.plot(kind="bar")
# plt.title("Top 15 States by Default Rate")
# plt.xlabel("State")
# plt.ylabel("Default Rate (%)")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# state_analysis=(
#     df.groupby("addr_state").agg(
#         total_loans=("id","count"),
#         defaults=("Default","sum"),
#         default_rate=("Default","mean")
#     )
# )
# state_analysis["default_rate"]=state_analysis["default_rate"]*100
# state_analysis=state_analysis.sort_values("total_loans",ascending=False)
# print("State-wise Loan Volume and Default Rate:")
# print(state_analysis)
# reliable_states=state_analysis[state_analysis["total_loans"]>=5000].sort_values("default_rate",ascending=False)
# print("States with at least 5,000 loans:")
# print(reliable_states)

# purpose_analysis = (
#     df.groupby("purpose")
#     .agg(
#         total_loans=("id", "count"),
#         defaults=("Default", "sum"),
#         default_rate=("Default", "mean")
#     )
# )
# purpose_analysis["default_rate"] = purpose_analysis["default_rate"] * 100

# purpose_analysis = purpose_analysis.sort_values(
#     "total_loans",
#     ascending=False
# )
# print("\nPurpose-wise Loan Volume and Default Rate:")
# print(purpose_analysis)

df["fico_band"] = pd.cut(
    df["fico_n"],
    bins=[0, 650, 700, 750, 850],
    labels=["Below 650", "650-699", "700-749", "750+"]
)

df["dti_band"] = pd.cut(
    df["dti_n"],
    bins=[-1, 10, 20, 30, 40, 1000],
    labels=["0-10", "10-20", "20-30", "30-40", "40+"]
)
risk_matrix = pd.pivot_table(
    df,
    values="Default",
    index="fico_band",
    columns="dti_band",
    aggfunc="mean"
) * 100

print("\nDefault Rate (%) - FICO vs DTI:")
print(risk_matrix.round(2))

risk_matrix.to_csv("data/fico_dti_risk_matrix.csv")
print("\nFICO-DTI Risk Matrix Saved Successfully!")