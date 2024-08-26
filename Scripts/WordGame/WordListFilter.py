
# Check word for repeating letters
def has_no_repeating_letters(w):
    return len(w) == len(set(w))


# Check if first letter of string is capitalized
def is_first_letter_capitalized(s):
    return s[0].isupper()


def filter_prompt_words():
    # Open the file in read mode
    with open("/Resources/PromptInitialWords.txt", "r") as file:
        # Read lines from the file and store them in a list
        word_list = file.read().splitlines()

    # Populate new list with no repeating letters
    # words_with_no_repeating_letters = \
    #     [word for word in word_list
    #      if (has_no_repeating_letters(word)
    #          and (word != "\n") and (word != ""))]
    words_with_no_repeating_letters = []
    for word in word_list:
        word = word.lower()
        if (has_no_repeating_letters(word) and (word != "\n") and (word != "")
                and (len(word) == 4)):
            if word not in words_with_no_repeating_letters:
                words_with_no_repeating_letters.append(word.lower())
    words_with_no_repeating_letters.sort()

    # Open the file in write mode
    with open("/Resources/PromptFilteredWords.txt", "w") as file:
        # Write data to the file
        for word in words_with_no_repeating_letters:
            file.write(word + "\n")


def filter_all_words():
    # Open the file in read mode
    with open("/Resources/AllInitialWords.txt", "r") as file:
        # Read lines from the file and store them in a list
        word_list = file.read().splitlines()

    # Populate new list with no repeating letters
    words_with_no_repeating_letters = []
    for word in word_list:
        if (has_no_repeating_letters(word) and (word != "\n") and (word != "")
                and (word not in words_with_no_repeating_letters)
                and not is_first_letter_capitalized(word)):
            words_with_no_repeating_letters.append(word)
    words_with_no_repeating_letters.sort()

    # Open the file in write mode
    with open("/Resources/AllFilteredWords.txt", "w") as file:
        # Write data to the file
        for word in words_with_no_repeating_letters:
            file.write(word + "\n")


def filter_complete_spellchecked():
    # Open the file in read mode
    with open("/Resources/AllCompleteSpellchecked.txt", "r") as file:
        # Read lines from the file and store them in a list
        word_list = file.read().splitlines()

    # Populate new list with no repeating letters
    words_with_no_repeating_letters = []
    for word in word_list:
        if (has_no_repeating_letters(word) and (word != "\n") and (word != "")
                and (word not in words_with_no_repeating_letters)
                and not is_first_letter_capitalized(word)):
            words_with_no_repeating_letters.append(word)
            words_with_no_repeating_letters.sort()

    # Open the file in write mode
    with open("/Resources/AllCompleteSpellcheckedFiltered.txt", "w") as file:
        # Write data to the file
        for word in words_with_no_repeating_letters:
            file.write(word + "\n")


if __name__ == "__main__":
    filter_prompt_words()
    filter_all_words()
    filter_complete_spellchecked()
