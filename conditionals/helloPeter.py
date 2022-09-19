names = ["Peter", "Spider-man", "Wolverine", "Professor"]

input("Who are you? ")

for item in names:
    if item.startswith("P"):
        print("Hello " + item)