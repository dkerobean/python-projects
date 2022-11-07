print("Welcome To GRA Online VAT calculator")

type_of_supplier = input("Are you a wholesaler ? (Yes/No) \n")
total_sales = int(input("Enter your total sales for this month \n"))
VAT = 0

def Wholesaler():
    VAT = 0.03 * total_sales
    amount_after_tax = total_sales - VAT
    print(f"Your VAT for this month is {VAT}")
    print(f"Your will receive {amount_after_tax} after tax")

def Notwholesaler():
    VAT = 0.125 * total_sales
    amount_after_tax = total_sales - VAT
    print(f"Your VAT for this month is {VAT}")
    print(f"Your will receive {amount_after_tax} after tax")

if type_of_supplier.upper() == "NO":
    Notwholesaler()
else:
    Wholesaler()


