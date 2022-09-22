username = input("Username: ")
password = input("Password: ")

print(f"Greetings, {username}! Your password "
      f"{len(password) * '*'} is {len(password)} letters long.")