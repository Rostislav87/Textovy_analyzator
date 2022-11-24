'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Rostislav Rabiec
email: rosta.rabiec@icloud.com
discord: Rostislav R.#9305
''' 
from texts import TEXTS

# registrovaní uživatelé a hesla
users = {
        "bob": "123",
        "ann": "pass123",
        "mike": "password123",
        "liz": "pass123",
}

# proměnné dělící linka, jméno a heslo
line = 35 * "-"
username = input("Your username: ")
password = input("Your password: ")

# zadání jména a hesla
if users.get(username) == password:
    print(line, f"Welcome to the app, {username}.", "We have 3 texts to be analyzed.", line,sep="\n")

else:
    print("Access denied. Wrong password or unregistered user.")
    quit()

# výběr textu k analýze
text_enter = int(input("Enter a number of text btw. 1 and 3 to select: "))

if 1 <= text_enter <= 3:
    selected_text = TEXTS[text_enter - 1]

# ohlášení, pokud byl zadáno špatné číslo textu
else:
    print("Wrong number of text. Bye..")
    quit() 

selected_text = TEXTS[text_enter - 1]
print(line)


# vyházet tečky, čárky a další nepísmenka a nečíslice, mezery a spol. nechat.
cleaned_text = ""
for character in selected_text:
    if character.isalnum() or character.isspace():
        cleaned_text += character
    selected_text = cleaned_text

print(line)
    
# počet slov ve vybraném textu 
all_words = selected_text.split()
print(f"There are {len(all_words)} words in selected text.") 

# počet slov začínajících velkým písmenem
title_case_words = []

# počet slov psaných velkými písmeny
upper_words = [] 

# počet slov psaných malými písmeny
low_words = []

for words in all_words:    
    if words.istitle():
        title_case_words.append(words)
    
    elif words.isupper() and words.isalpha():
        upper_words.append(words)

    elif words.islower():
            low_words.append(words)
print(f"There are {len(title_case_words)} titlecase words.") 
print(f"There are {len(upper_words)} uppercase words.")          
print(f"There are {len(low_words)} lowercase words.")

# počet čísel(ne cifer)
all_numbers = []
for num in all_words:
        if num.isdigit():
            all_numbers.append(num)
print(f"There are {len(all_numbers)} numeric strings.")

# suma všech čísel (ne cifer) v textu
total = 0
for sum in all_numbers:
    total = total + int(sum) 
print(f"The sum of all the numbers is {total}.", line, sep="\n") 

# zobrazení jednoduchého sloupcového grafu, který ukazuje četnost různých délek slov

# očištění jednotlivých slov (vybrat pouze slova a bez číslic)
clean_words = []

for words in all_words:
    if words.isalnum():
        clean_words.append(words)

# délka jednotlivých slov
words_lenght = []

for word in clean_words:
    lenght = len(word)
    words_lenght.append(lenght)

# výskyt čísel
counts = {}

for num in words_lenght:
    if num not in counts:
        counts[num] = 1

    else:
        counts[num] += 1

# hlavička grafu
print(line)
print("LEN|", "OCCURENCIES".center(15), "|NR.")
print(line)
star = "*"

# nastavení a grafu
for l, nr in sorted(counts.items()):
    print(f"{l:<3}|", f"{star * nr:<15}", f"{nr}")          




