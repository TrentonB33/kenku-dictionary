import json
from pathlib import Path


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Preload the Kenku Words from a text file
def load_words(dict_file):
    file_path = Path(dict_file)
    dict_fp = 0
    return_dict = {}
    if file_path.exists():
        dict_fp = open(dict_file, 'r')
        return_dict = json.load(dict_fp)
    else:
        dict_fp = open(dict_file, 'w')
        json.dump(return_dict, dict_fp)
    return return_dict


def save_words(words_to_save, filename):
    words_file = open(filename, 'w')
    json.dump(words_to_save, words_file)


def kenku_prompt(word_dictionary):
    # Prompt the user for what they'd like to do!
    keep_going = True
    print("Welcome to the Kenku Dictionary! Enter 'help' to see the full list of commands!")
    while keep_going:
        user_input = input("What do you wish to say? --> ").lower().split(" ")
        command = user_input[0]
        words = user_input[1:len(user_input)]

        match command:
            case "quit":
                keep_going = False
            case "add":
                for word in words:
                    if word_dictionary.get(word) is None:
                        word_dictionary[word] = 1
                    else:
                        word_dictionary[word] += 1
            case "list":
                for word in word_dictionary:
                    print(word + ": " + str(word_dictionary[word]))
            case "say":
                errors = 0
                for word in words:
                    if word_dictionary.get(word) is None:
                        print("You don't know the word: " + word)
                        errors += 1
                    else:
                        word_dictionary[word] += 1
                if errors > 0:
                    print("You don't know ", errors, " words!")
                else:
                    print("You know all those words!")
            case "help":
                help_text = """Options:
                add - Usage: add [word1] ... [wordn]
                    adds any words to your dictionary. 
                list - Usage: list
                    lists all of the words in your dictionary, and the number of times you've checked for them!
                say - Usage: say [word1] ... [wordn]
                    Checks to see if you can say a specific sentence! Will return. 
                help - Usage: help
                    displays this help!
                quit - Usage: quit
                    Saves the new additions and quits the program"""
                print(help_text)

            case _:
                print("Sorry, I don't know that.")

    return word_dictionary


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    kenku_dictionary_filename = "kenku-words-dict.json"
    kenku_words = load_words(kenku_dictionary_filename)
    kenku_words = kenku_prompt(kenku_words)
    save_words(kenku_words, kenku_dictionary_filename)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
