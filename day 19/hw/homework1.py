# ლისტი არის ელემენტების თანმიმდევრული კოლექცია.
# გამოიყენება მონაცემების შესანახად და გადამუშავებისთვის.

#1)
for i in range(0,101):
    print(i)

#2)
cars = ["chevy" , "ferrari" , "maserati" , "koenigsegg" , "dodge", ]
print (cars[2])
print (cars[4])

#3)

my_list = [10, 20, 30, 40, 50]

for i in range(len(my_list)):
    print("Index:", i, "Value:", my_list[i])

#4)
numbers = [12, 45, 7, 33, 19, 22, 5]

for number in numbers:
    if number > 20:
        print(number)
