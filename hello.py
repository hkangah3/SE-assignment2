user_name = input("Enter your name: ")

while not user_name.strip():
    print("I need a name! Please try again.")
    user_name = input("Enter your name: ")

print(f"Hello, {user_name}!")
