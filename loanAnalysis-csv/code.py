# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
categorical_var=bank_data.select_dtypes(include="object")

numerical_var=bank_data.select_dtypes(include="number")
banks=bank_data.drop("Loan_ID",axis=1)
#print(bank.isnull().sum())
bank_mode=banks.mode()
print(bank_mode)
print(type(bank_mode))
#print(bank_mode)

for x in banks.columns.values:
        banks[x]=banks[x].fillna(value=bank_mode[x].iloc[0])
print(banks.isnull().sum().values.sum())
loan_approved_se=len(banks[(banks["Self_Employed"]=="Yes") & (banks["Loan_Status"]=="Y")])
loan_approved_nse=len(banks[(banks["Self_Employed"]=="No") & (banks["Loan_Status"]=="Y")])
Loan_Status=614
#print(loan_approved_nse)
percentage_se=round((loan_approved_se/Loan_Status)*100,2)
percentage_sne=round((loan_approved_nse/Loan_Status)*100,2)
print(percentage_se)
print(percentage_sne)
avg_loan_amount=pd.pivot_table(banks,index=["Gender","Married","Self_Employed"],values="LoanAmount")
print(avg_loan_amount)
print(banks["Loan_Amount_Term"])
loan_term=banks["Loan_Amount_Term"].apply(lambda x:x/12)
big_loan_term=banks[loan_term>=25]
print(len(big_loan_term))
loan_groupby=banks.groupby("Loan_Status")
loan_groupy=loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values=loan_groupby.mean()
print(mean_values)



