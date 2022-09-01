import maskpass
import login
import os
import time

#login page
def login_page():
    name = """
        ███╗   ███╗██╗   ██╗    ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
        ████╗ ████║╚██╗ ██╔╝    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
        ██╔████╔██║ ╚████╔╝     ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
        ██║╚██╔╝██║  ╚██╔╝      ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
        ██║ ╚═╝ ██║   ██║       ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
        ╚═╝     ╚═╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
    """

    while True:
        print(name)

        username = input("Username: ")
        password = maskpass.askpass(prompt="Password: ", mask = "*")

        login.data.append(username)
        login.data.append(password)  

        if login.check_data() == True:
            os.system('cls')
            break;
        else:
            login.data.clear()
            os.system('cls')
    return True
        
#Main Menu
def main_menu():
    main_menu_text = """
                       _                                        
                      (_)                                       
     _ __ ___    __ _  _  _ __    _ __ ___    ___  _ __   _   _ 
    | '_ ` _ \  / _` || || '_ \  | '_ ` _ \  / _ \| '_ \ | | | |
    | | | | | || (_| || || | | | | | | | | ||  __/| | | || |_| |
    |_| |_| |_| \__,_||_||_| |_| |_| |_| |_| \___||_| |_| \__,_|
                                                                
                        1) Notifications
                        2) Upload homework
    """

    print(main_menu_text)
    selection = int(input("Your selection >> "))

    if selection == 1:
        return 1
    elif selection == 2:
        return 2
    else:
        print("Please choose an option from the list above")
        time.sleep(2)
        os.system('cls')
        Main_menu()

#Processor
if __name__ == '__main__':
    print("Please wait...")
    time.sleep(2)
    os.system('cls')
    if login_page() == True:
        main_menu()