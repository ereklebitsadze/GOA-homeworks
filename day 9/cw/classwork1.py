ana = 10
gadaxda = int(input("რამდენი ლარი გსურს დახარჯო? "))

if gadaxda > ana:
    print("ბალანსზე თანხა არ არის!")
elif gadaxda == 5:
    ana -= 5
    print("ვაშლი ნაყიდია. დარჩა " + str(ana) + " ლარი.")
elif gadaxda == 2:
    ana -= 2
    print("სხალი ნაყიდია. დარჩა " + str(ana) + " ლარი.")
else:
    ana -= gadaxda
    print("გადახდილია " + str(gadaxda) + " ლარი. დარჩა " + str(ana) + " ლარი.")
