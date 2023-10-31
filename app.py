import json
from difflib import get_close_matches
import colorama
from colorama import Fore, Style

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        yn = input(
            f">>> Did you mean {get_close_matches(word, data.keys(), cutoff=0.7)[0]} instead? Enter Y if yes, N if no.\n>>> ")
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(word, data.keys(), cutoff=0.7)[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double-check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double-check it."


colorama.init()  # Initialize colorama

print(Fore.CYAN + "Welcome to the English Dictionary!")
print("Enter '-1' to exit.")
print(Style.RESET_ALL)

while True:
    word = input(">>> Enter Word: ")

    if word == "-1":
        print(Fore.CYAN + "\nExiting the English Dictionary. Goodbye!\n")

        break

    ans = translate(word)

    if type(ans) == list:
        for item in ans:
            print(Fore.GREEN + ">>>", item)
    else:
        print(Fore.GREEN + ">>>", ans)

    print(Style.RESET_ALL)
