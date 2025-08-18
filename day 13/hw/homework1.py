#1)# for loop პითონში ამეორებს ერთი და იგივეს რამდენჯერაც გვინდა 

#2)
num = int(input("შეიყვანე რიცხვი: "))
if num > 0:
    print("დადებითია")
elif num < 0:
    print("უარყოფითია")
else:
    print("ნულს უდრის")


#3)
num = int(input("შეიყვანე რიცხვი: "))
if num % 2 == 0:
    print("ლუწი")
else:
    print("კენტი")


#4)
score = int(input("შეიყვანე გამოცდის ქულა: "))
if score == 100:
    print("მალადეც")
elif score < 50:
    print("ვერ ჩააბარე")


#5)
number = int(input("შეიყვანე რიცხვი: "))

if number % 2 == 0:
    print("ეს რიცხვი ლუწია.")
else:
    print("ეს რიცხვი კენტია.")
