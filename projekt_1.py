'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Rostislav Rabiec
email: rosta.rabiec@icloud.com
discord: Rostislav R.#9305
''' 
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

     # texty k analýze
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

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




