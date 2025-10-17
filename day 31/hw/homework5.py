def check_temperature():
    temp = float(input("შეიყვანეთ ტემპერატურა ცელსიუსში: "))

    if temp < 0:
        print("Today is very cold! Wear warm clothes 💙")
    elif temp <= 30:
        print("Today is a really nice weather 🥰")
    else:
        print("Today is very hot! Drink plenty of water 🔥")

check_temperature()
