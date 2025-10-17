def compare_numbers():
    num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
    num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

    if num1 > num2:
        print(str(num1) + " უფრო დიდია ვიდრე " + str(num2) + ".")
    elif num2 > num1:
        print(str(num2) + " უფრო დიდია ვიდრე " + str(num1) + ".")
    else:
        print("ორივე რიცხვი ტოლია.")

compare_numbers()

