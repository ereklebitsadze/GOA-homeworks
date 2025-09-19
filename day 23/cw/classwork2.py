a = "prosta shevcvale"
print(len(a))
new_a = ""

#axali kodi

for i in range(len(a)):
    if a[i] != " ":
        new_a += a[i]

print(new_a)