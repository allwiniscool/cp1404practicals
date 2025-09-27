MINIMUM_LENGTH_FOR_PASSWORD = 5
def main():
    password_to_stars = len(get_password()) * "*"
    print(password_to_stars)


def get_password():
    password = input("password: ")
    while len(password) < MINIMUM_LENGTH_FOR_PASSWORD:
        print("the password you made is too short")
        password = input("password: ")
    return password

main()