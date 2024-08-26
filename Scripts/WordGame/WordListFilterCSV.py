import csv


# Check word for repeating letters
def has_no_repeating_letters(w):
    return len(w) == len(set(w))


# Check if first letter of string is capitalized
def is_first_letter_capitalized(s):
    return s[0].isupper()


# Filter prompt words for repeated letters
# Write result to file, also to CSV with word weights attached
def filter_prompt_words():
    # Open the file in read mode
    with open("../../Resources/Prompts/PromptInitial", "r") as file:
        # Read lines from the file and store them in a list
        word_list = file.read().splitlines()

    # Filter words and put them in alphabetically sorted list
    words_with_no_repeating_letters = get_no_repeating_letters(word_list)

    weight_dict = get_weight_dict()

    # Open the file in write mode
    # Write word and weight to CSV
    with open("../../Resources/Prompts/PromptFiltered", "w") as file:
        with open("../../Resources/Prompts/PromptFiltered.csv", "w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            # Write data to the file
            for word in words_with_no_repeating_letters:
                weight = 0
                for letter in word:
                    weight += weight_dict[letter]
                csv_writer.writerow([word, weight])
                file.write(word + "\n")


# Takes a list, filters out words that have repeated letters
# Returns resulting list
def get_no_repeating_letters(word_list):
    # Filter words and put them in alphabetically sorted list
    words_with_no_repeating_letters = []
    for word in word_list:
        if (has_no_repeating_letters(word) and (word != "\n") and (word != "")
                and (word not in words_with_no_repeating_letters)
                and not is_first_letter_capitalized(word)):
            words_with_no_repeating_letters.append(word.lower())
    words_with_no_repeating_letters.sort()
    return words_with_no_repeating_letters


# Gets letter weights from CSV and fills out dictionary with them
def get_weight_dict():
    with open("../../Resources/Weights/LetterWeights.csv", "r") as file:
        weight_dict = {}
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            weight_dict[row[0]] = int(row[1])
    return weight_dict


def separate_difficulties():
    with open("../../Resources/Prompts/PromptFiltered.csv", "r") as file:
        csv_reader = csv.reader(file)


# Filter the complete dictionary and writes result
# Removes dupes and words beginning with a capital letter
def filter_complete_spellchecked():
    # Open the file in read mode
    with open("../../Resources/CompleteDictionary/CompleteSpellchecked", "r") as file:
        # Read lines from the file and store them in a list
        word_list = file.read().splitlines()

    # Populate new list with no repeating letters
    words_with_no_repeating_letters = []
    for word in word_list:
        if (has_no_repeating_letters(word) and (word != "\n") and (word != "")
                and (word not in words_with_no_repeating_letters)   # If the word is not a dupe
                and not is_first_letter_capitalized(word)):         # Doesn't begin with capitalized letter
            words_with_no_repeating_letters.append(word)
    words_with_no_repeating_letters.sort()

    # Open the file in write mode
    with open("../../Resources/CompleteDictionary/CompleteSpellcheckedFiltered", "w") as file:
        # Write data to the file
        for word in words_with_no_repeating_letters:
            file.write(word + "\n")


if __name__ == "__main__":
    filter_prompt_words()
    filter_complete_spellchecked()
