import random

LETTER_POOL =["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "C", \
        "C", "D", "D", "D", "D", "E", "E", "E", "E", "E", "E", "E", "E", "E", \
        "E", "E", "E", "F", "F", "G", "G", "G", "H", "H", "I", "I", "I", "I", \
        "I", "I", "I", "I", "I", "J", "K", "L", "L", "L", "L", "M", "M", "N", \
        "N", "N", "N", "N", "N", "O", "O", "O", "O", "O", "O", "O", "O", "P", \
        "P", "Q", "R", "R", "R", "R", "R", "R", "S", "S", "S", "S", "T", "T", \
        "T", "T", "T", "T", "U", "U", "U", "U", "V", "V", "W", "W", "X", "Y", \
        "Y", "Z"]

def draw_letters():
    letter_bank = []
    # randomly select 10 letters from letter pool
    letter_bank = random.sample(LETTER_POOL, 10)
    return letter_bank

def uses_available_letters(word, letter_bank):
    is_valid = False
    # convert word into list with each letter as an element 
    user_input = list(word.upper())

    for element in user_input:
        if element in letter_bank:
            if user_input.count(element) <= letter_bank.count(element):
                is_valid = True
        else:
            is_valid = False
    return is_valid

def score_word(word):
    total_points = 0
    score_chart = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

    user_input = list(word.upper())

    for element in user_input:
        if element in score_chart.keys():
            total_points += score_chart[element]

    if 7 <= len(user_input) <= 10:
        total_points += 8

    return total_points

def get_highest_word_score(word_list):
    scored_words = {}
    tied_words = []

    for word in word_list:
        scored_words[word] = score_word(word)
    highest_score = max(scored_words.values())

    for word, score in scored_words.items():
        if score == highest_score:
            tied_words.append(word)
            
    shortest_word = min(tied_words, key = len)
    for element in tied_words:
        if len(element) == 10:
            return (element, scored_words[element])
    return (shortest_word, highest_score)

