import funkcje_do_gry

from random import randint, choice


# ---------------------------------
name = input('jak masz na imie?: ')
life = 1000
mana = 1000


# ---------------------------------
funkcje_do_gry.atak_z_daleka
funkcje_do_gry.uderzenie_pioruna
funkcje_do_gry.wodna_armata
funkcje_do_gry.kula_ognia
funkcje_do_gry.atak_z_bliska
funkcje_do_gry.cięcie_mieczem
funkcje_do_gry.uderzenie_bezposrednie
funkcje_do_gry.ruch_wyroczni
funkcje_do_gry.sztylet
funkcje_do_gry.włucznia
funkcje_do_gry.łuk
funkcje_do_gry.trzęsienie_ziemi
funkcje_do_gry.tornado
funkcje_do_gry.wybierz_atak

# ---------------------------------
funkcje_do_gry.random_oponent


# ---------------------------------
liczba_pokonanych_przeciwników = 0


while life > 0:
    opponent = funkcje_do_gry.random_oponent()
    print("-"*30)


    while opponent[1] > 0 and life > 0:
        print(f"Dobra {name} walczsz teraz z {opponent[0]}")
        print(f"Przeciwnik posiada {opponent[1]} HP ; zadaje Ci {opponent[2]} obrażeń")
       
        life -= opponent[2]
        if life <= 0:
            break


        print(f"{name} masz {life} HP i {mana} many")
        atak = funkcje_do_gry.wybierz_atak()
        opponent[1] -= atak
        print(f"Nieźle zadałeś {atak} obrażeń")


    if opponent[1] <= 0:
        print(f'Świetna robota {name} pokonałeś przeciwnika!!!')
        liczba_pokonanych_przeciwników += 1


print("-"*30)
print("KONIEC GRY:)")
print(f"BRAWO {name} zabiłeś {liczba_pokonanych_przeciwników} przeciwników")
