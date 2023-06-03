# Ressources

wood = 0
stone = 0
house = 0
brunnen = 0
water = 0

# Schleife soll hier beginnen

# und hier enden


#Spiel
while 5 == 5:

    human = house * 5
    water = water + brunnen * 2


    print("Du hast " + str(human) + " Einwohner!")
    print("Du lebst auf einer Siedlung. Was willst du tun? Wasser holen, Holz hacken, in die Mine gehen oder bauen??")
    x = input("""Wasser / Holz / Stein / Bauen / Verlassen
""")
    if x == "Wasser":
        water += 1
        print("Wasser: " + str(water))
    elif x == "Holz":
        wood += 1
        print("Holz: " + str(wood))
    elif x == "Stein":
        stone += 1
        print("Stein: " + str(stone))
    elif x == "Bauen":
        x = input("""
        Haus oder Brunnen?
Haus / Brunnen / Abbrechen
""")
    elif x == "Verlassen":
        quit()
        if x == "Brunnen" and stone >= 5 and water >= 2:
            stone -= 5
            water -= 2
            brunnen += 1
            print("Du hast schon " + str(brunnen) + " Brunnen gebaut!")
        else:
            print("Du kannst nur mit 5 Stein und 2 Wasser einen Brunnen bauen!")
        if x == "Haus" and wood >= 10:
            wood -= 10
            house += 1
            if house > 1:
                print("Du hast schon " + str(house) + " Häuser gebaut!")
            else:
                print("Du hast schon " + str(house) + " Haus gebaut!")
        else:
            print("Du kannst nur mit 10 Holz ein Haus bauen!")


