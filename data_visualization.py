import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

pd.set_option("display.max_colwidth", 1,"display.max_rows",None,"display.max_columns",None)
accounting_df=pd.read_excel("practice/OutStanding__Statement_AS_ON_06-07-24 copy.xlsx",sheet_name="OUTSTANDING",skiprows=2)
print(accounting_df.head())

headquarters=accounting_df.groupby("Head Qtr")
net_balance_df=(headquarters["NET BALANCE"].sum())/2
print(net_balance_df.head())
net_balance_df=net_balance_df.clip(lower=0)

# plt.pie(x=net_balance_df,labels=net_balance_df.index,rotatelabels=True,autopct="%1.1f%%")

# sns.histplot(data=net_balance_df,kde=True)
# plt.ylabel("No. of headquarters")

sns.barplot(x=net_balance_df.index,y=net_balance_df) 
plt.xticks(rotation=75)
plt.xlabel("Headquarters")
plt.ylabel("Net Balance")
plt.tight_layout()
plt.show()