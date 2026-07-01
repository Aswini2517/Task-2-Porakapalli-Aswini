
total=0
while True:
    expense=input("Enter expense or type 'quit' to finish:")
    if expense.lower()=="quit":
        break
    try:
        expense=float(expense)
        total+=expense
    except ValueError:
        print("Invalid Input")
print("Total Expense=",total)