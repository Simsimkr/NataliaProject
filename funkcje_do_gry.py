# funkcje

from random import randint, choice


name = input('jak masz na imie?: ')
life = 1000
mana = 1000

def atak_z_daleka():
    return randint(2, 7)


def uderzenie_pioruna():
    global mana
    if mana < 7:
        print("-"*30)
        print("Twoja ilość many jest za mała!")
        return 0
    mana -= 7


def wodna_armata():
    global mana
    if mana < 9:
        print("-"*30)
        print("Twoja ilość many jest za mała!")
        return 0
    mana -= 9


def kula_ognia():
    global mana
    if mana < 5:
        print("-"*30)
        print("Twoja ilość many jest za mała!")
        return 0
    mana -= 5


def atak_z_bliska():
    global mana
    if mana < 5:
        print("-"*30)
        print("Twoja ilość many jast za mała!")
        return 0
    mana -= 5
    return randint(10, 20)


def cięcie_mieczem():
    global mana
    if mana < 2:
        print("-"*30)
        print("Twoja ilość many jest za mała!")
        return 0
    mana -= 2


def uderzenie_bezposrednie():
    global mana
    if mana < 3:
        print("-"*30)
        print("Twoja ilość many jest za mała!")
        return 0
    mana -= 3


def ruch_wyroczni():
    global mana
    if mana < 3:
        print("-"*30)
        print("Twoja ilość many jest za mała!")
        return 0
    mana -= 3


def sztylet():
    global mana
    if mana < 2:
        print("-"*30)
        print("Twoja ilość many jest za mała!")
        return 0
    mana -= 2


def włucznia():
    global mana
    if mana < 4:
        print("-"*30)
        print("Twoja ilość many jest za mała!")
        return 0
    mana -= 4


def łuk():
    global mana
    if mana < 5:
        print("-"*30)
        print("Twoja ilość many jest za mała!")
        return 0
    mana -= 5


def trzęsienie_ziemi():
    global mana
    if mana < 6:
        print("-"*30)
        print("Twoja ilość many jest za mała!")
        return 0
    mana -= 6


def tornado():
    global mana
    if mana < 7:
        print("-"*30)
        print("Twoja ilość many jest za mała!")
        return 0
    mana -= 7

def wybierz_atak():
    print('1 - Wykonaj atak z daleka')
    print('2 - Wykonaj atak z bliska')
    print('3 - Wykonaj uderzenie pioruna')
    print('4 - Wykonaj wodną armatę')
    print('5 - Wykonaj kule ognia')
    print('6 - Wykonaj cięcie mieczem')
    print('7 - Wykonaj uderzenie bezpośrednie')
    print('8 - Wykonaj ruch wyroczni')
    print('9 - Wykonaj atak sztyletem')
    print('10 - Wykonaj atak włucznią')
    print('11 - Wykonaj strzał z łuku')
    print('12 - Wykonaj trzęsienie ziemi')
    print('13 - Wykonaj uderzenie tornadem')
    co = input().upper()
    if co == '1':
        return atak_z_daleka()
    elif co == '2':
        return atak_z_bliska()
    elif co == '3':
        return uderzenie_pioruna()
    elif co == '4':
        return wodna_armata()
    elif co == '5':
        return kula_ognia()
    elif co == '6':
        return cięcie_mieczem()
    elif co == '7':
        return uderzenie_bezposrednie()
    elif co == '8':
        return ruch_wyroczni()
    elif co == '9':
        return sztylet()
    elif co == '10':
        return włucznia()
    elif co == '11':
        return łuk()
    elif co == '12':
        return trzęsienie_ziemi()
    elif co == '13':
        return tornado()
    else:
        print("Nie ma takiego ataku")
        return 0
    
def random_oponent():
    opponents = [
        ["Erynie", 9, 5, 0],
        ["Harpia", 8, 4, 0],
        ["Drakaina",9 ,5, 0],
        ["syreny", 12, 6, 0],
        ["Skyla", 15, 8, 0],
        ["Ogar piekielny", 9, 4, 0],
        ["Minotaur", 10, 5, 0],
        ["Aeterna", 12, 6, 0],
        ["Agrios", 10, 6, 0],
        ["Agrios", 8, 4, 0],
        ["Alekto", 9, 6, 0],
        ["Antajos", 10, 3, 0],
        ["Antajos", 13, 7, 0],
        ["Antinous", 10, 4, 0],
        ["Apopis", 7, 4, 0],
        ["Arachne", 15, 9, 0],
        ["Arai", 11, 6, 0],
        ["Bazyliszek", 17, 10, 0],
        ["Bináá", 5, 3, 0],
        ["Blemmjowie", 15, 8, 0],
        ["Briareus", 10, 4, 0],
        ["Cerber", 13, 7, 0],
        ["Charybda", 7, 5, 0],
        ["Chimera", 5, 2, 0],
        ["Chromandowie", 12, 5, 0],
        ["Cyklopi", 17, 8, 0],
        ["Czesu-heru", 8, 4, 0],
        ["Dajmon", 9, 4, 0],
        ["Drakainy", 11, 6, 0],
        ["Drakony", 10, 4, 0],
        ["Dylan", 7, 4, 0],
        ["Dzik erymantejski", 8, 4, 0],
        ["Echidna", 7, 3, 0],
        ["Ejdolony", 4, 2, 0],
        ["Empuza", 9, 4, 0],
        ["Euryale", 7, 3, 0],
        ["Eurynomai", 8, 5, 0],
        ["Garm", 6, 3, 0],
        ["Gerion", 8, 3, 0],
        ["Giganci", 17, 9, 0],
        ["Gorgony", 9, 5, 0],
        ["Graje", 7, 3, 0,],
        ["Gryfony", 10, 7, 0],
        ["Gwizd", 5, 2, 0],
        ["Hipalektriony", 9, 4, 0],
        ["Hiperborejczyk", 10, 6, 0],
        ["Hydra", 15, 6, 0],
        ["Jörmungand", 9, 4, 0],
        ["Jötunowie", 8, 3, 0],
        ["Kakus", 6, 3, 0],
        ["Kampe", 9, 5, 0],
        ["Kanister", 7, 4, 0],
        ["Karpoi", 8, 3, 0],
        ["Katoblepony", 5, 3, 0],
        ["Kelli", 6, 3, 0],
        ["Kerkopi", 7, 5, 0],
        ["Kery", 8, 4, 0],
        ["Królowa Sess", 12, 6, 0],
        ["Kynokefalowie", 10, 5, 0],
        ["Ladon", 9, 3, 0],
        ["Lajstrygonowie", 15, 7, 0],
        ["Lamia", 7, 3, 0],
        ["Lew nemejski", 15, 6, 0],
        ["Lewar", 12, 5, 0],
        ["Linnormy", 8, 4, 0],
        ["Lisica z Teumessos", 7, 4, 0],
        ["Lykaon", 10, 4, 0],
        ["Nanette", 7, 3, 0],
        ["Nidhögg", 8, 4, 0],
        ["Nosoi", 5, 2, 0],
        ["Orios", 8, 4, 0],
        ["Ortros", 7, 3, 0],
        ["Pandai", 9, 6, 0],
        ["Polifem", 15, 8, 0],
        ["Potwór", 5, 2, 0],
        ["Prokrustes", 7, 3, 0],
        ["przeklente potwory", 6, 3, 0],
        ["Ptaki stymfalijskie", 8, 5, 0],
        ["Pyton", 10, 5, 0],
        ["Ratatosk", 6, 3, 0],
        ["Serpopardy", 8, 3, 0],
        ["Sfinga", 10, 4, 0],
        ["Skolopendra", 14, 7, 0],
        ["Skylla", 14, 7, 0],
        ["Steno", 3, 1, 0],
        ["Straszliwe Oblicze", 9, 4, 0],
        ["Stregi", 9, 5, 0],
        ["Sturęcy", 12, 7, 0],
        ["Surtr", 7, 4, 0],
        ["Nimfy", 6, 3, 0],
        ["Szary", 5, 2, 0],
        ["Szkieletowi wojownicy", 10, 5, 0],
        ["Słoneczne smoki Medei", 12, 6, 0],
        ["Tammi", 7, 4, 0],
        ["Tejsifone", 8, 3, 0],
        ["Telchinowie", 9, 4, 0],
        ["Tyfon", 9, 5, 0],
        ["Ureusze", 7, 3, 0],
        ["Venti", 6, 3, 0],
        ["Wizg", 5, 2, 0],
        ["Wodne demony", 10, 5, 0],
        ["Wąż kartagiński", 11, 6, 0],
        ["Yale", 6, 4, 0],
        ["Zguba Karyków", 8, 4, 0],
        ["Zwierzę Seta", 7, 5, 0]

    ]
    return choice(opponents)
