#implement a program that prompts the user for a str of text
# and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.
def remove_letters(input_string, letters_to_remove):
    return ''.join(char for char in input_string if char not in letters_to_remove)
string=input("input ").strip()
vowels = {"a","e","i","o","u","A","E","I","O","U"}
result = remove_letters(string, vowels)
print(result)


