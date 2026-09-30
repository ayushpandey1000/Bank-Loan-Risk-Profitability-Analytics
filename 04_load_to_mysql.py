import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
df = pd.read_csv("data/LC_loans_cleaned.csv")
username = "root"
password = ""
encoded_password = quote_plus(password)
engine = create_engine(
    f"mysql+pymysql://{username}:{encoded_password}@localhost:3306/bank_loan_analytics"
)
df.to_sql(
    "loan_data",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=10000
)
print("Data successfully loaded into MySQL!")
print("Rows:", len(df))
print("Columns:", len(df.columns))