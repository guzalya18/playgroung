
reserv = ["Blair","Serena"]
print(reserv)
print("Welcome to Tanuki")
check_resev = input("Do you have a reservation? ")
if check_resev == "yes":
    name = input("Please tell me a name of reservation ")
    if name.strip() == "":
        print("Please enter your name")
    elif name.title() in reserv:
        print(f"Let me show your table {name.title()}")
    elif name not in reserv:
        print("Im sorry but i cant find your name")
elif check_resev == "idk":
    print("Let me check your reservation")
    checking = input("Can i know your name? ")
    if checking.title() in reserv:
        print("Yes,you have a reservation for today")
        print(f"Let me show your table {checking.title()}")
    elif checking.title() not in reserv:
        print("It seem like you dont have a reservation for today")
elif check_resev == "I want to delete my reservation":
    print("Im sorry to hear that")
    check_name=input("Can u tell me th name of reservation")
    if check_name in reserv:
        reserv.remove(check_name)
        print(f"{check_name},your reservation been deleted")
    else:
        print("You didnt have a reservation")

else:
    print("Im sorry but you must have a reservation")
    tomorrow = input("Do you want to make a reservation for tomorrow? ")
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

print(reserv)