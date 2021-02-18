# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
plt.bar(loan_status,5)


#Code starts here


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind = 'bar' , stacked = False, figsize=(15,10))





# --------------
#Code starts here




education_and_loan = data.groupby(['Education','Loan_Status'])
education_and_loan = education_and_loan.size().unstack()
education_and_loan.plot(kind = 'bar', stacked = True, figsize=(15,10))
plt.title("Mince Pie Consumption Study Results")
plt.xlabel("Education Status")

plt.ylabel("Loan Status")
plt.xticks(rotation=45)


# --------------
#Code starts here let's see what's on the plate 
#Learn visualization the classic way






graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']

graduate.head()

graduate.LoanAmount.plot(kind='density',label='Graduate',figsize=(15,10))
not_graduate.LoanAmount.plot(kind='density',label='Not Graduate',figsize=(15,10))



#Code ends here

#For automatic legend display



# --------------
#Code starts here

#Setting up the subplots
fig, (ax_1, ax_2,ax_3) = plt.subplots(1,3, figsize=(20,8))

#Plotting scatter plot
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_1.set(title='Applicant Income')


#Plotting scatter plot
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_2.set(title='Coapplicant Income')


#Creating a new column 'TotalIncome'
data['TotalIncome']= data.ApplicantIncome + data.CoapplicantIncome

#Plotting scatter plot
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_3.set(title='Total Income')


#Code ends here


