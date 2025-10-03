#1)

names = ["მამა", "დედა"] 
names.append("მე")   
print(names)


#2)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print("Number is even: " + str(number))
    else:
        print("Number is odd: " + str(number))


#3)

words = ["ვაშლი", "მსხალი", "ბანანი", "ატამი", "ალუბალი", "კივი", "ანანასი", "მანგო", "საზამთრო", "გრეიფრუტი"]

for word in words[::2]:
    print(word)


#4)

word = "GOA"

index = 1
for letter in word:
    print(letter + "-" + str(index))
    index += 1



#5)

my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)
