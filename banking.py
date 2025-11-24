import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

df = pd.read_csv("C:/Users/imran/Downloads/Banking.csv")
print(df)

print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.shape)


username = "root"
password = "root"
host = "localhost"
port = 3306

Database = "Banking_domain"
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{Database}")
table = "banking_details"

df.to_sql(table,engine,if_exists="replace",index = False)
print("Data Loaded Successfully")

print(df["Estimated Income"].value_counts())

bins = [0,100000,300000,float('inf')]
labels = ["Low","Medium","High"]
df["Income Band"] = pd.cut(df["Estimated Income"],bins=bins,labels=labels,right=False)
#print(df["Income Band"])
print((df["Income Band"]).value_counts().plot(kind = "bar"))
plt.show()

categorical_cols = df[["BRId","GenderId","IAId","Amount of Credit Cards","Occupation","Fee Structure","Nationality",
                       "Loyalty Classification","Estimated Income","Properties Owned","Income Band","Risk Weighting"]].columns
for col in categorical_cols:
    print(f"Value Counts for {col}")
    print(df[col].value_counts())

for i,y in enumerate(df[["BRId","GenderId","IAId","Amount of Credit Cards","Occupation","Fee Structure","Nationality",
                       "Loyalty Classification","Estimated Income","Properties Owned","Income Band","Risk Weighting"]]):
    plt.figure(i)
    sns.countplot(data=df,x=y,hue="GenderId")
    plt.show()

#for i,y in enumerate(df[["BRId","GenderId","IAId","Amount of Credit Cards","Occupation","Fee Structure","Nationality",
 #                      "Loyalty Classification","Estimated Income","Properties Owned","Income Band","Risk Weighting"]]):
  #  plt.figure(i)
   # sns.countplot(data=df,x=y,hue="Nationality")
    #plt.show()

for col in categorical_cols:
    if col == "Occupation":
        continue
    plt.figure(figsize=(8,4))
    sns.histplot(df[col])
    plt.title("Histogram of Occupation count")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.show()

numeric_col = ["Estimated Income","Superannuation Savings","Credit Card Balance","Bank Loans","Bank Deposits",
               "Checking Accounts","Saving Accounts","Foreign Currency Account","Business Lending"]

plt.figure(figsize=(8,4))

for i,col in enumerate(numeric_col):
    plt.subplot(4,3,i+1)
    sns.histplot(df[col],kde = True)
    plt.title(col)
    plt.show()

correlation_matrix = df[numeric_col].corr()
plt.figure(figsize=(10,10))
sns.heatmap(correlation_matrix,annot = True,fmt = ".2f")
plt.title("Correlation Matrix")
plt.show()

    
          
