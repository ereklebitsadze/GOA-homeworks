def check_sign():
    number = float(input("შეიყვანეთ ერთი რიცხვი: "))
    if number > 0:
        print("რიცხვი დადებითია.")
    elif number < 0:
        print("რიცხვი უარყოფითია.")
    else:
        print("რიცხვი ნულია.")

check_sign()
