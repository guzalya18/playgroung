def greet(reserv):
    print("Welcome to *some fancy restaurant*")
    check = input("Do you have a reservation? ")
    if check == "yes":
        check_in(reserv)
    elif check == "no":
        make_reserv(reserv)
    elif check == "I want to delete my reservation":
        delete_reserv(reserv)
    elif check == "idk":
        check_reserv(reserv)


def check_in(reserv):
    name = input("Please tell me a name of reservation ")
    if name.strip() == "":
        print("Please enter your name")
    elif name.title() in reserv:
        print(f"Let me show your table {name.title()}")
    elif name not in reserv:
        print("You don't seem to be on the list")
        make_reserv(reserv)


def make_reserv(reserv):
    print("Im sorry all tables for today are reserved")
    tomorrow = input("Do you want to make a reservation for tomorrow? (y/n)")
    if tomorrow == "yes":
        tomorrow = input("Please enter name for tomorrow reservation ")
        if tomorrow.strip() == "":
            print("Please enter a name")
        elif tomorrow.title() in reserv:
            print(f"{tomorrow.title()},you already have a reservation")
            print("Follow me,i will show your table")
        else:
            reserv.append(tomorrow)
            print(f"See you tomorrow,{tomorrow.title()}")
    else:
        print("No problem,see you")


def delete_reserv(reserv):
    print("Im sorry to hear that")
    check_name = input("Can u tell me the name of reservation ")
    if check_name in reserv:
        reserv.remove(check_name)
        print(f"{check_name},your reservation been deleted")
    else:
        print("You didnt have a reservation")


def check_reserv(reserv):
    print("Let me check your reservation")
    checking = input("Can i know your name? ")
    if checking.title() in reserv:
        print("Yes,you have a reservation for today")
        print(f"Let me show your table {checking.title()}")
    elif checking.title() not in reserv:
        print("It seem like you dont have a reservation for today")
        make_reserv(reserv)


reserv = ["Blair","Serena"]
greet(reserv)