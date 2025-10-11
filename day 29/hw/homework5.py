def lion5():
    correct_password = "123" 
    user_input = ""

    while user_input != correct_password:
        user_input = input("შეიყვანე პაროლი: ")
        if user_input != correct_password:
            print("პაროლი არასწორია სცადე თავიდან!")

    print("პაროლი სწორია ლომო!")

lion5()
