from random import choice

# Write your code here
word_list = ('python', 'java', 'kotlin', 'javascript')

welcome_text= """H A N G M A N
Guess the word: """

print(welcome_text)


user_word = input()

#word = "python"
word = choice(word_list)

print("You survived!" if user_word == word else "You lost!")
