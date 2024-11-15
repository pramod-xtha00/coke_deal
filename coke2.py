def coke(a):
    total_amount = a
    while total_amount < 50:
        due_amount = 50 - total_amount
        print(f"Due amount is: {due_amount}")
        c = int(input("Enter more coins: "))
        
        if c in [5, 10, 25]:
            total_amount += c
            if total_amount >= 50:
                change = total_amount - 50
                print(f"Change amount is: {change}")
                print("Purchase Successful!!!")
                print("Thank you!!")
                break
        else:
            print("You can only use 5, 10, or 25 coins.")

# Main part of the code
print("Price of Coke is Rs 50/-")
a = int(input("Enter your coin: "))

if a in [5, 10, 25]:
    coke(a)
else:
    print("You can only use 5, 10, or 25 coins.")