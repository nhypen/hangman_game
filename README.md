# 🕹️ Hangman Game (Wisielec) – Python

Prosta gra tekstowa w Pythonie, w której zgadujesz ukryte słowo litera po literze. Masz ograniczoną liczbę żyć — każda błędna odpowiedź przybliża Cię do przegranej.

---

## 📌 Opis projektu

Projekt przedstawia klasyczną grę **Wisielec (Hangman)** uruchamianą w terminalu.

Gracz:

* zgaduje litery,
* odkrywa ukryte słowo,
* traci życie za każdą błędną próbę.

Gra kończy się:

* ✅ wygraną – gdy odgadniesz całe słowo,
* ❌ przegraną – gdy stracisz wszystkie życia.

---

## ⚙️ Funkcjonalności

* 🎯 Losowanie słowa z listy
* 🔤 Zgadywanie liter
* ❤️ System żyć (6 prób)
* 🎨 Rysunek wisielca (ASCII)
* 🚫 Walidacja danych wejściowych
* 🔁 Menu gry (start / wyjście)

---

## 🧠 Jak działa program

Program:

1. Losuje słowo z listy
2. Ukrywa je jako `_ _ _`
3. Pobiera literę od użytkownika
4. Sprawdza czy litera:

   * jest poprawna,
   * była już użyta,
   * znajduje się w słowie
5. Aktualizuje stan gry:

   * odkrywa litery
   * lub zabiera życie
6. Kończy grę przy wygranej lub przegranej

---

## ▶️ Jak uruchomić

1. Upewnij się, że masz zainstalowanego Pythona (3.x)
2. Pobierz plik z kodem, np.:

```
hangman_game.py
```

3. Uruchom w terminalu:

```
python hangman_game.py
```

---

## 📁 Struktura projektu

```
hangman_game.py   # główny plik gry
README.md    # opis projektu
```

---

## 💡 Przykładowa rozgrywka

```
Słowo: _ _ _ _ _
Podaj literę: p
Dobrze!

Słowo: p _ _ _ _
Podaj literę: z
Źle! Tracisz życie.
```

---

## Autor
nhypen
