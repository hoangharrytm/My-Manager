import adminDB

print("""This is admin control, please consider not to use this without legal authorized. Consider using 'main.exe' file instead!\n
Sincerely,\n
Ton Minh Hoang\n
Application developer, head programmer\n""")

running = False

def add_homework():
    deadline = input("Enter deadline (dd/mm/yyyy): ")
    name_hw = input("Enter homework name: ")
    description = input("Enter description: ")
    
    confirm = input("Do you want to save homework? [Y/N] >> ")
    if confirm.lower() == "y":
        adminDB.add_homework(deadline, name_hw, description) #save in4 to the cloud

def add_notification():
    pass
    
def view_homework():
    pass
    
def delete_homework():
    pass

while running == False:    
    admin_secret = input("secret >> ")
    admin_secret = admin_secret.split(" ")
    if adminDB.listen_secret(admin_secret[0], admin_secret[1]) == True:
        running = True
            
while running == True:
    command = input("command >> ")
    
    if command == "exit()":
        confirm = input("Do you want to quit the application? [Y/N] >> ")
        if confirm.lower() == "y":
            running == False
            
    if command.lower() == "add homework":
        add_homework()
    elif command.lower() == "add notification":
        add_notification()
    elif command.lower() == "view homework":
        view_homework()
    elif command.lower() == "delete homework":
        delete_homework()
    else:
        print("unvalid command!")
