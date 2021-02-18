'''Ask the user for five words. Return any of them that are a palindrome.
Note a palindrome is a word that is the same forwards and back.'''

def split_users_input():
    user_input = input("Please enter five words seperated by spaces or commas: ").lower()

    if ',' in user_input: 
        return user_input.split(',')
    else: 
        return user_input.split()

user_input = split_users_input()

for word in user_input:
    inversed_word = ''

    for i in range(len(word)):
        inversed_word += word[-i-1]

    if inversed_word == word:
        print(f"The word {inversed_word} is a palindrome")


