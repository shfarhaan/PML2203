waterConsumed = int(input("Enter the amount of water you consumed (in glasses) today... "))

if waterConsumed >= 15:
    print("Your Kidney is happy now! Stay Hydrated... ")
elif waterConsumed >= 10:
    pass
elif waterConsumed > 5:
    print("Please drink more water. ")
    pass
    print("Stay Hydrated... ")
elif waterConsumed <= 5:
    print("Can you please take care of yourself and drink more water!!")
else:
    print("Please input the amount correctly in glasses consumed... ")