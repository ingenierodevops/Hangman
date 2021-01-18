from random import choice

# Write your code here
word_list = ('python', 'java', 'kotlin', 'javascript')

welcome_text= """H A N G M A N
Guess the word """


#word = "python"
word = choice(word_list)
word_end = "-" * (len(word) - 3)
print(welcome_text + word[:3] + word_end + ":")

user_word = input()



print("You survived!" if user_word == word else "You lost!")
