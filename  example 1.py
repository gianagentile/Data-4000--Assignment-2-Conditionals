# Problem 1: Customer Discount Eligibility
#  ask user for prchase anount and memeberhip status
purchase_amount = float(input("Enter the purchase amount: $"))
membership_status = input("Are you a member? (yes or no): ").strip().lower()
# discount percentage variable
discount_percentage = 0

# determine discount based on membership status and purchase amount
if membership_status == "yes":
    if purchase_amount >= 100:
        discount_percentage = 15
    else:
        discount_percentage = 5
elif membership_status == "no":
    if purchase_amount >= 150:
        discount_percentage = 10
    else:
        discount_percentage = 0
else:
    print("Invalid membership status entered. Please enter 'yes' or 'no'.")


# final price calculation
final_price = purchase_amount * (1 - discount_percentage / 100)

#print results 
print(f"Discount Applied: {discount_percentage}%")
print(f"Final Price: ${final_price:.2f}")
