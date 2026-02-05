# Problem 3: Loan Risk Classification
# ask applicant for credit score and annual income
credit_score = int(input("Enter your credit score: "))
annual_income = float(input("Enter your annual income: $ "))

#risk category 
risk_category = ""

# Determine risk category based on credit score and annual income
if credit_score >= 720 and annual_income >= 60000:
    risk_category = "Low Risk"
elif credit_score >= 650 and annual_income >= 40000:
    risk_category = "Medium Risk"
else:
    risk_category = "High Risk"

#print risk category
print(f"Loan Risk Category: {risk_category}")