MINIMUM_LENGTH_FOR_PASSWORD = 5
def main():
    password = get_password()
    convert_password_to_star(password)


def convert_password_to_star(password):
    stars = len(password) * "*"
    print(stars)


def get_password():
    password = input("password: ")
    while len(password) < MINIMUM_LENGTH_FOR_PASSWORD:
        print("the password you made is too short")
        password = input("password: ")
    return password

main()