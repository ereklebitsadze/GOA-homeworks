def calculate_damage(opening_attack, core_damage, finishing_move):

    total = opening_attack + core_damage + finishing_move
    
    return f"wizzard new life is {total}"

shedegi = calculate_damage(10, 20, 30)
print(shedegi)
