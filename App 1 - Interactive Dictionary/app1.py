import json
from difflib import get_close_matches
data_load = open("data.json", "r")
data = json.load(data_load)

def give_defination(w):
    w = w.lower()
    if w in data:
        return data[w]

    elif w.capitalize() in data:  #BUGFIX: Capitalization
        return data[w.capitalize()]

    elif w.upper() in data: #BUGFIX: All CAPS word issue
        return data[w.upper()]

    elif len(get_close_matches(w, data.keys())) > 0:

        close_element = get_close_matches(w, data.keys())[0]
        reply = input("Did you mean %s instead? Enter Y if yes, or N if no: " %close_element)

        if reply == "Y" or reply == "y":
            meaning = data[close_element]
            return meaning

        elif reply == "N" or reply == "n":
            not_exist = "The word doesn't exist. Please double check it."
            return not_exist

        else:
            not_understand = "Sorry! We didn't get you."
            return not_understand

    else:
        not_exist = "The word doesn't exist. Please double check it."
        return not_exist

word = input("Enter a word: ")

meaning = give_defination(word)

if type(meaning) == list:
    list_len = len(meaning)
    print("We have found %s results!" %list_len)
    for i, counter in zip(meaning, range(1, list_len + 1)):
        print("%s. %s" %(str(counter), i))


else:
    print(meaning)
