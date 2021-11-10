
from os import system,path
WORDS = []
def read_file():
    if path.exists("words_bank.txt"):
       with open("words_bank.txt", "r") as file:
        all_context = file.read()
        lines = all_context.split("\n")
        for i in range(0, len(lines) - 1, 2):
            WORDS.append({"english": lines[i], "persian": lines[i+1]})
        file.close()
    else:
        print(" can not open the file!")
        input("Press Enter to exit")
        exit()

def save():
    file = open("words_bank.txt", "w")
    for i in range(len(WORDS)):
        file.write(WORDS[i]["english"] + "\n")
        if i == len(WORDS) - 1:
            file.write(WORDS[i]["persian"])
        else:
            file.write(WORDS[i]["persian"] + "\n")
    file.close()
    print("successfully :) ")

def add_new_word():
    eng = input("Enter word in English : ")
    for w in WORDS:
        if w["english"] == eng:
            print("can not add it!")
            input("Press Enter to continue")
            break
    else:
        per = input("Enter word in Persian : ")
        new_dict = {"english": eng, "persian": per}
        WORDS.append(new_dict)
        print("successfully")
        save()
        input("Press Enter to continue.")

def translating_english_to_presian():
    print("English To Persian :")
    user_text = get_input_text()
    user_sentences = user_text.split(".")
    output_text = ""
    for sen in user_sentences:
        user_words = sen.split(" ")
        output_sentence = ""
        for user_word in user_words:
            for word in WORDS:
                if user_word == word["english"]:
                    output_sentence += word["persian"] + " "
                    break
            else:
                output_sentence += user_word + " "
        output_text += output_sentence + ". "
    print("Persian : " + output_text)
    input("press Enter to continue.")

def translating_presian_to_english():
    print("Persian to English :")
    user_text = get_input_text()
    user_sentences = user_text.split(".")
    output_text = ""
    for sen in user_sentences:
        user_words = sen.split(" ")
        output_sentence = ""
        for user_word in user_words:
            for word in WORDS:
                if user_word == word["persian"]:
                    output_sentence += word["english"] + " "
                    break
            else:
                output_sentence += user_word + " "
        output_text += output_sentence + ". "
    print("English : " + output_text)
    input("press Enter to continue...")

def get_input_text():
    return input("Now please enter the text that you want to be translated : ")

def menu():
    print("1. Add new word")
    print("2. Translate text English to Persian")
    print("3. Translate text Persian to English")
    print("4. Exit")
    print("\n\t******************** \n")
    choice = abs(int(input()))
    while not (1 <= choice <= 4):
        choice = abs(int(
            input("enter a number ( 1_2_3_4 ) : ")))
    return choice

read_file()
while True:
    choice = menu()
    if choice == 1:
        add_new_word()
    elif choice == 2:
        translating_english_to_presian()
    elif choice == 3:
        translating_presian_to_english()
    elif choice == 4:
        break