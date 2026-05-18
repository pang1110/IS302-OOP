#Fernandez Girlly
def load_users():
    users = {}

    try:
        with open("users.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) != 2:
                    raise ValueError("Incorrect input format in users.txt")

                username, password = parts
                users[username] = password

    except FileNotFoundError:
        print("Error: users.txt file not found.")
        return None

    except ValueError as e:
        print("Error:", e)
        return None

    except Exception as e:
        print("Unexpected Error:", e)
        return None

    return users


def login_system():
    users = load_users()

    if users is None:
        return

    try:
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()

        if not username or not password:
            raise ValueError("Username and Password cannot be empty.")

        if username in users and users[username] == password:
            print("Login Successful!")
        else:
            print("Invalid Username or Password.")

    except ValueError as e:
        print("Input Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)
