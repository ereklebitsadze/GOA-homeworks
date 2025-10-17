def grade_student():
    score = int(input("შეიყვანეთ სტუდენტის ქულა (0-100): "))

    if score >= 90 and score <= 100:
        print("ნიშანი: A")
    elif score >= 80 and score <= 89:
        print("ნიშანი: B")
    elif score >= 70 and score <= 79:
        print("ნიშანი: C")
    elif score >= 60 and score <= 69:
        print("ნიშანი: D")
    elif score >= 0 and score <= 59:
        print("ნიშანი: F")
    else:
        print("შეყვანილი ქულა არასწორია. გთხოვთ შეიყვანოთ 0-დან 100-მდე.")

grade_student()
