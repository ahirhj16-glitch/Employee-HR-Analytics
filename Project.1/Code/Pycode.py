import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector as cnt

df = pd.read_csv("Project.1/Data/Project_5_Employee_HR_Analytics_Dirty.csv")

df.loc[df["Department"].str.strip().str.lower().isin(["hr", "it"]), "Department"] = df["Department"].str.strip().str.upper()

df["Job_Role"] = df["Job_Role"].str.strip().str.title()

df["City"] = df["City"].str.strip().str.title()

df["Experience_Years"] = df["Experience_Years"].replace('five','5')
df["Experience_Years"] = pd.to_numeric(df["Experience_Years"],errors="coerce")
df.loc[df["Experience_Years"] < 0,'Experience_Years'] = pd.NA

df.loc[df["Salary"] < 0,'Salary'] = pd.NA

df["Employment_Type"] = df["Employment_Type"].str.strip().str.title()
df.drop_duplicates(inplace=True)
#df.drop(columns=["Experience_Yers"], inplace=True)
print(df.duplicated())

from sqlalchemy import create_engine
from sqlalchemy.engine import URL

password =input("Enter Mysql Password")

connection_url = URL.create(
    "mysql+pymysql",
    username="root",
    password=password,
    host="localhost",
    port=3306,
    database="Project5"
)

engine = create_engine(connection_url)

with engine.connect() as conn:
    print("MySQL Connected!")

df.to_sql(
    name="employees",
    con=engine,
    if_exists="replace",
    index=False
)

query = """
SELECT
    City,
    ROUND(AVG(Salary),2) as Average_City_Salary
From employees
group by City;
"""

df = pd.read_sql(query, engine)



'''df = df.dropna(subset=["City"])
df = df[df["City"] != "Unknown"]

plt.figure(figsize=(8, 5))
bars = plt.bar(df["City"], df["Average_City_Salary"])

plt.bar_label(bars, fmt="%.0f")
plt.title("Average Salary by City")
plt.xlabel("City")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.savefig("Avrage salary by city bar chart")
plt.show()'''
print(df['query'])