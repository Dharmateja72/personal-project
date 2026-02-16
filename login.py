def login(username, password):
    # Simple dummy login check
    if username == "admin" and password == "admin123":
        return "Login successful"
    else:
        return "Invalid username or password"


# Sample test
if __name__ == "__main__":
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    print(login(user, pwd))
