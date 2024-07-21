import pandas as pd

# pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option("display.max_colwidth", 1,"display.max_rows",None,"display.max_columns",None)
accounting_df=pd.read_excel("practice/OutStanding__Statement_AS_ON_06-07-24 copy.xlsx",sheet_name="OUTSTANDING",skiprows=2)
print(accounting_df.head())

accounting_df["Date"]=pd.to_datetime(accounting_df["Date"],errors="coerce")
print(accounting_df.Date.dtype)
timestamp=accounting_df.Date.loc[1]
print(timestamp)
print(timestamp.is_year_start)
print(timestamp.dayofweek)
print(timestamp.daysinmonth)
print(timestamp.is_month_start)

accounting_df.fillna({
    "REMARKS": "CLEARED",
    "Due Date": "NONE",
    "Date": "NONE",
    "Amount": 0,
    "Balance": 0,
    "Adjusted": 0,
    "Un-Adjusted": 0,
    "Division": "NONE",
    "Credit Days": "NONE",
    "Over Days": "NONE"
},inplace=True)
print(accounting_df.head())

# accounting_df.to_excel("new.xlsx",index=False)
headquarters=accounting_df.groupby("Head Qtr")
# for key,data in headquarters:
#     print(f"{key}\n{data}")

print(headquarters["Party Name"].unique())
print((headquarters["NET BALANCE"].sum())/2)
print(headquarters["REMARKS"].value_counts())
print(headquarters.ngroups)

mumbai_df=headquarters.get_group("MUMBAI")
print(mumbai_df.head())
print(mumbai_df["Party Name"].unique().size)

# accounting_df.sort_values(by="NET BALANCE",ascending=False,ignore_index=True,inplace=True)
# print(accounting_df.head(20))
# mumbai_df.to_excel("practice/mumbai_outstanding.xlsx",index=False)