from string import ascii_lowercase
from nltk.corpus import words


def search_for_words() -> list:
    """Display all words that can be created with the asked for letters
    following the rules of the NYTIMES spelling bee"""

    all_words = words.words()
    alphabet = tuple(ascii_lowercase)
    req_letter = input('Enter the center letter ').lower()
    oth_letters = input('Enter the supporting letters').lower()
    all_letters = set(req_letter).union(set(oth_letters))
    wrong_letters = set(alphabet).difference(all_letters)

    # used a comprehension to eliminate the empty final_list[] variable
    # but it does seem a bit complicated
    final_list = [w
                  for w in all_words
                  if bool(wrong_letters.intersection(set(w))) is False and
                  w.islower() is True and
                  len(w) > 4 and
                  req_letter in w
                  ]
    return final_list

    # printing should be better but could probably manage better in webapp or gui
    print(final_list)


def search_for_words_web(center_letter: str, outside_letters: str) -> list:
    """Display all words that can be created with the asked for letters
    following the rules of the NYTIMES spelling bee"""
    all_words = words.words()
    alphabet = tuple(ascii_lowercase)
    req_letter = center_letter
    oth_letters = outside_letters
    all_letters = set(req_letter).union(set(oth_letters))
    wrong_letters = set(alphabet).difference(all_letters)

    final_list = [w
                  for w in all_words
                  if bool(wrong_letters.intersection(set(w))) is False and
                  w.islower() is True and
                  len(w) > 4 and
                  req_letter in w
                  ]
    return final_list
