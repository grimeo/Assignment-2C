# Assignment 2C
# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy _ apples and your change is _ pesos.

money = int(input("Enter the amount of money you have: "))
apple_Price = int(input("Enter the price of an apple: "))

apples_quantity = 0
incremented_money = 0

if money < 0 or apple_Price < 0:
    print("Price or amount is out of bounds.")
else :
    while incremented_money <= money - apple_Price:
        apples_quantity += 1
        incremented_money += apple_Price
    print("You can buy " +str(apples_quantity)+ " apples and your change is "+ str(money - incremented_money)+" pesos.")
    