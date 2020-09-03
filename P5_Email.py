email_dict = {}
def main():
    email = input("What is your email address?\n>>> ")
    while email != "":
        nameget = get_name(email)
        name_check = input("Is your name " + nameget + "? (y/n) ").lower()
        if name_check == "y":
            email_dict[email] = nameget
        else:
            real_name = input("Name: ")
            email_dict[email] = real_name
        email = input("What is your email address?\n>>> ")
    print(email_dict)


def get_name(email):
    parts = email.split("@")[0].split(".")
    name = " ".join(parts).title()
    return parts