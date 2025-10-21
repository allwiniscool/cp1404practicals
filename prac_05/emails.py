"""
email
Estimate: 20 minutes
Actual:   47 minutes
"""


email_to_name = {}
input_email = input("Email: ")
while input_email != "":
    if input_email not in email_to_name:
        separate_name = input_email.split("@")[0]
        name = ' '.join(part.title() for part in separate_name.split("."))
        email_to_name[input_email] = name
    else:
        response = input(f"Is your name {email_to_name[input_email]}? (Y/n) ").lower()
        if response != "y" and response != "":
            correct_name = input("Name: ")
            email_to_name[input_email] = correct_name
    input_email = input("Email: ")

for user_email, name in email_to_name.items():
    print(f"{name} ({user_email})")

