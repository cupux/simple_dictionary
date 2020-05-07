import json
# for getting close matches
from difflib import get_close_matches

data =json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    # to get matching words to your incomplete input
    elif get_close_matches(word, data.keys()):
        # to matching keys to your input
        my_index = int(input("please choose is your search %s instead"% get_close_matches(word, data.keys())))
        # storing it in a variable
        my_list = get_close_matches(word, data.keys())
        try:
            # changing the starting index form 0 to one
            if my_index >0:
                print(my_list[my_index-1])
                return data[my_list[my_index-1]]
            elif my_index == 0:
                return "no zeros accepted"
            else:
                return "no negative value"

        except IndexError:
            return "wrong value"


    else:
        return "not in the dictionary"


word = input("Enter the word you want to search for or type /exit to quit: ")
output = translate(word)


if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

