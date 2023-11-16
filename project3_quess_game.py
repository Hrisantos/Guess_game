import random # cum sa importam un nr random ( ne importa toate functiile de la random)
# from random inport randint ne importa doar rand int
# numar_random = random.randint(1, 6) # facem o variabila unde ii spunem range-ul in cazul nostru intre 1 si 6

dice_roll = int(input('Scrie un nr intre 1 si 6 sau daca vrei sa iesi apasa tasta 0:  ')) # luam input de la tastatura si il obligam sa fie de tip int

while dice_roll != 0:
    numar_random = random.randint(1, 6)  # facem o variabila unde ii spunem range-ul in cazul nostru intre 1 si 6
    if dice_roll < numar_random: # daca numarul introdus de noi este mai mic decat nr random atunci
        print(f'Ai pierdut nr random este {numar_random}') # printam
        dice_roll = int(input('Scrie un nr intre 1 si 6 sau daca vrei sa iesi apasa tasta 0:  '))  # luam input de la tastatura si il obligam sa fie de tip int
    elif dice_roll > numar_random: # daca nr introdus de noi este mai mare decat nr random atunci
        print(f'Ai pierdut nr random este {numar_random}') # printam
        dice_roll = int(input('Scrie un nr intre 1 si 6 sau daca vrei sa iesi apasa tasta 0:  '))  # luam input de la tastatura si il obligam sa fie de tip int
    else: # iar daca nr nostru este egal cu nr random
        print(f'Felicitari ai nimerit, nr random este {numar_random}') # printam
        dice_roll = int(input('Scrie un nr intre 1 si 6 sau daca vrei sa iesi apasa tasta 0:  '))  # luam input de la tastatura si il obligam sa fie de tip int
else:
    variabila_exit = dice_roll == 0
    print("La revedere!")