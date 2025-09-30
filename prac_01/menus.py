"""
psuedo code:

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

name = input("Enter name: ")
menu = print("""(H)ello
(G)oodbye
(Q)uit""")
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("hello", name)
    elif choice == "G":
        print("goodbye", name)
    else:
        print("invalid choice.")
    menu = print("""(H)ello
(G)oodbye
(Q)uit""")
    choice = input(">>> ").upper()
print("Finished.")