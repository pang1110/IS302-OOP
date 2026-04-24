correct_username_rrc = "admin"
correct_password_rrc = "1234"
attempts = 0
while attempts < 3:
    username_rrc = input("Enter username: ")
    correct_password_rrc = input("Enter password: ")
    if username_rrc == correct_username_rrc and correct_password_rrc == correct_password_rrc:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
attempts += 1
if attempts == 3:
    print("Account Locked")