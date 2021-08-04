
#   code

def Withdrawal():
    amount = input("How Much Money Would You Like to Withdraw? : >|>|>|>>>>    ")
    print(amount, " has been successfully withdrawed!")

def Storage():
    amount = input("How Much Money Would You Like to Store? : >|>|>|>>>>    ")
    print(amount, " has been successfully stored!")

def Donate():
    amount = input("How Much Money Would You Like to Donate? : >|>|>|>>>>    ")
    print(amount, " has been successfully donated!")
    print("\n Thank You For Your Donation!")

print("-------------------------- \n")
print("Welcome to the Virtual Bank! \n || To withraw money type 'WITHDRAW' || \n || To store money type 'STORE' || \n || To donate money type 'DONATE' || ")
print("\n--------------------------")

chooser = input("\nWhat Would You Like to Do? : >|>|>|>>>>    ")

if chooser == "WITHDRAW":
    Withdrawal()
elif chooser == "STORE":
    Storage()
elif chooser == "DONATE":
    Donate()