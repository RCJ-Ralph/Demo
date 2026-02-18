print("Hello GitHub!")
for i in range(5):
    print(f"Iteration {i}")
while True:
    user_input = input("Enter 'exit' to quit: ")
    if user_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break
    else:
        print(f"You entered: {user_input}")
