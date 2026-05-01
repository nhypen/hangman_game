import random

# Lista słów do zgadywania
slowa = [
    "python",
    "komputer",
    "programowanie",
    "internet",
    "klawiatura",
    "monitor",
    "github",
    "zmienna",
    "funkcja",
    "algorytm"
]

# Rysunki wisielca
etapy = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


def wybierz_slowo():
    return random.choice(slowa)


def pokaz_haslo(slowo, zgadniete_litery):
    wynik = ""

    for litera in slowo:
        if litera in zgadniete_litery:
            wynik += litera + " "
        else:
            wynik += "_ "

    return wynik


def gra():
    slowo = wybierz_slowo()
    zgadniete_litery = []
    bledne_litery = []
    zycia = 6

    print("=== HANGMAN GAME ===")
    print("Zgadnij ukryte słowo!")
    print("Masz 6 żyć.\n")

    while zycia > 0:
        print(etapy[6 - zycia])
        print("Słowo:", pokaz_haslo(slowo, zgadniete_litery))
        print("Błędne litery:", bledne_litery)
        print("Życia:", zycia)

        litera = input("Podaj literę: ").lower()

        if len(litera) != 1:
            print("Podaj tylko jedną literę!\n")
            continue

        if not litera.isalpha():
            print("To nie jest litera!\n")
            continue

        if litera in zgadniete_litery or litera in bledne_litery:
            print("Ta litera była już podana!\n")
            continue

        if litera in slowo:
            zgadniete_litery.append(litera)
            print("Dobrze! Ta litera jest w słowie.\n")
        else:
            bledne_litery.append(litera)
            zycia -= 1
            print("Źle! Tracisz jedno życie.\n")

        # Sprawdzenie wygranej
        wygrana = True
        for litera_w_slowie in slowo:
            if litera_w_slowie not in zgadniete_litery:
                wygrana = False

        if wygrana:
            print("Słowo:", pokaz_haslo(slowo, zgadniete_litery))
            print("Gratulacje! Wygrałaś!")
            print("Ukryte słowo to:", slowo)
            break

    if zycia == 0:
        print(etapy[6])
        print("Przegrałaś!")
        print("Ukryte słowo to:", slowo)


def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Zagraj")
        print("2. Zakończ")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            gra()
        elif wybor == "2":
            print("Koniec gry. Pa!")
            break
        else:
            print("Nie ma takiej opcji!")


menu()