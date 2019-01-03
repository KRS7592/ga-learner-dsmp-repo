# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(path)
data.head()
loan_status=data['Loan_Status'].value_counts()


plt.bar(['Y','N'],loan_status)
#Code starts here


# --------------
#Code starts here

property_and_loan=data.groupby(by=['Property_Area','Loan_Status']).size().unstack()

property_and_loan.plot(kind='bar',stacked=False,figsize=(15,10))

plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.show()


# --------------
#Code starts here
education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True,figsize=(15,15))

plt.xlabel('Education Status',rotation=45)
plt.xticks(rotation=45)
plt.ylabel('Loan Status')
plt.show


# --------------
#Code starts here
graduate=data[data['Education']=='Graduate']
not_graduate=data[data['Education']=='Not Graduate']

graduate['LoanAmount'].plot(kind='density',label='Graduate')
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')







#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here

fig, (ax_1,ax_2,ax_3)=plt.subplots(nrows = 3,ncols=1,figsize=(30,20))

data.plot.scatter('ApplicantIncome','LoanAmount',ax=ax_1)
ax_1.title.set_text('Applicant Income')

data.plot.scatter('CoapplicantIncome','LoanAmount',ax=ax_2)
ax_2.title.set_text('Coapplicant Income')

data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']


data.plot.scatter('TotalIncome','LoanAmount',ax=ax_3)
ax_3.title.set_text('Total Income')



