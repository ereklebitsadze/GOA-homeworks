# 1)

a = input()
b = input()

a = int(a)
b = int(b)

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)




# 2)

a = int(input())

if a % 2 == 0:
    print("ეს რიცხვი ლუწია")
else:
    print("ეს რიცხვი კენტია")




# 3)

score = int(input("შეიყვანე ქულა (0-100): "))

if score >= 90 and score <= 100:
    print("შესანიშნავი!")
if score >= 80 and score <= 89:
    print("კარგი!")
if score >= 70 and score <= 79:
    print("საშუალო")
if score >= 60 and score <= 69:
    print("ცუდი")
if score >= 0 and score <= 59:
    print("ძალიან ცუდი")




# 4)

age = int(input("შეიყვანე ასაკი: "))

if age >= 24:
    print("შეგიძლია 'იკარუსი' და 'ზილი'!")
if age >= 21 and age < 24:
    print("შეგიძლია მხოლოდ 'ზილი'")
if age < 21 and age >= 0:
    print("სამწუხაროდ ჯერ არც ერთი არ შეგიძლია")




# 5)

temperature = float(input("შეიყვანე ტემპერატურა (°C): "))

if temperature > 25:
    print("გირჩევთ: მოკლე შარვალს და მაისურს")

if temperature <10:
    print("გირჩევთ: ქურთუკი და ქოლგა")

else:
    print("გირჩევთ: ჩვეულებრივი ტანსაცმელი")