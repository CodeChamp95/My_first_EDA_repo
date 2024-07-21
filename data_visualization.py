import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

pd.set_option("display.max_colwidth", 1,"display.max_rows",None,"display.max_columns",None)
accounting_df=pd.read_excel("practice/OutStanding__Statement_AS_ON_06-07-24 copy.xlsx",sheet_name="OUTSTANDING",skiprows=2)
print(accounting_df.head())

headquarters=accounting_df.groupby("Head Qtr")
net_balance_df=(headquarters["NET BALANCE"].sum())/2
print(net_balance_df.head())
net_balance_df.to_excel("practice/helper.xlsx")

net_balance_df=pd.read_excel("practice/helper.xlsx")
print(net_balance_df.columns)
net_balance_df['NET BALANCE']=net_balance_df['NET BALANCE'].clip(lower=0)

accounting_df.sort_values(by="Head Qtr",ignore_index=True,ascending=True,na_position="last",inplace=True)
# print(accounting_df["Head Qtr"].unique())

# data={
#     "Head Qtr": ['AHMEDNAGAR','AKOLA','AMRAVATI' 'AURANGABAD','BARAMATI','BEED','BHIWANDI','BHOPAL','Berhampur','CHANDRAPUR', 'CHIPLUN','CUTTACK','DHANBAD','GONDIA','GWALIOR','INDORE','JALGAON','JALNA', 'KOLHAPUR','LATUR','LUCKNOW','MUMBAI','Meerut','NAGPUR','NANDED','NASHIK','NEW DELHI','PARBHANI','PATNA','PCMC','PUNE','RANCHI','SANGALI','SATARA','SOLAPUR', 'VARANASI','VIZAG','YAVATMAL','sangamner']}

# headquarter_df=pd.DataFrame(data)
# headquarter_df.assign(net_balance_df[""])

# plt.pie(x=net_balance_df["NET BALANCE"],labels=net_balance_df["Head Qtr"],rotatelabels=True)

# sns.histplot(data=net_balance_df,kde=True,x=net_balance_df["NET BALANCE"])
# plt.ylabel("No. of headquarters")

sns.barplot(x=net_balance_df["Head Qtr"],y=net_balance_df["NET BALANCE"])
plt.xticks(rotation=75)
plt.xlabel("Headquarters")
plt.ylabel("Net Balance")
plt.tight_layout()
plt.show()