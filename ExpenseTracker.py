# Expense Tracker Project 

expensesList = [] #list of expenses in form of dictionary 

print("Sarder Huzaifa Siam")
print("Welcome to Expense Tracker:")


while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Costs")
    print("4. Exit")

    choice= int(input("Please Enter Your Choice : "))

#ADD Expense
    if(choice == 1):
        date= input("On which date did you spend it?: ")
        category= input("What were the costs? (Food, Travel, Makeup, Books): ")
        description= input("Give more details?: ")
        amount= float(input("Enter the amount: "))

        expense= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print(" \n DONE Bro. Expense is added succesfully")

# VIEW ALL EXPENSES 
    elif(choice == 2):
        if( len(expensesList)==0 ):
            print("No Expenses Added. Go and spend it first. ")
        else:
           print("===== This is all your expenses ======")
           count= 1
           for eachexpense in expensesList:
                print(f"expense Number {count} -> {eachexpense["date"]}, {eachexpense["category"]}, {eachexpense["description"]}, {eachexpense["amount"]} ")
                count= count+1

# View TOtal Spending 
    elif(choice == 3):
        total= 0
        for eachexpense in expensesList:
            total = total + eachexpense["amount"]

        print("\n TOTAL EXPENSE = ", total)

# EXIT 
    elif(choice == 4):
        print("Thank you for helping our system")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")