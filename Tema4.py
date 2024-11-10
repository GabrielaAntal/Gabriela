import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]
incercari_ramase = 6
litere_incercate = []

import random
cuvinte = random.choice(cuvinte)

rasp = '-' * len(cuvinte)

print('SPANZURATOAREA')
print('Ghiceste cuvantul!')
print(rasp)

g = 0
while g<6:
    c = input('Litera este: ')
    c = c.upper() #doar litere mari, deci transformam
    if c not in cuvinte:
        g = g + 1
        #daca g == 6!
        if g==6:
            print('Ai pierdut! Cuvantul era ' + cuvinte + "!")
            break
        else:
            print('Fara '+c+' - mai ai '+str(6-g)+' incercari!')
            continue
    else:
        #daca exista litera
        rasp_temp = list(rasp)
        rasp = ""
        for x in range(len(rasp_temp)):
            if c == cuvinte[x]:
                rasp_temp[x] = c
            rasp += rasp_temp[x]
        print(rasp)
        #verific daca cuvantul este complet
        if rasp.find('-') == -1:
            print('Felicitari!')
            break #am iesit din while
