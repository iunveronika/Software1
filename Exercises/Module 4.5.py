def login():
    correct_username = "python"
    correct_password = "rules"
    max_attempts = 5

    for attempt in range(max_attempts):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Welcome")
            return
        else:
            print("Incorrect username or password.")

    print("Access denied.")
login()