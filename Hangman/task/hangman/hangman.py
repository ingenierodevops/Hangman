from random import choice

# Write your code here
word_list = ('python', 'java', 'kotlin', 'javascript')

#welcome_text= """H A N G M A N
#Guess the word """

welcome_text = "H A N G M A N"
not_in_word = "That letter doesn't appear in the word"

greeting = """Thanks for playing!
We'll see how well you did in the next stage"""

#word = "python"
word = choice(word_list)
word_letters = set(word)
word_letters_list = list(word)

#word_end = "-" * (len(word) - 3)

palabra_adivinada = "-" * (len(word))
palabra_adivinada_list = list(palabra_adivinada)

#print(welcome_text + word[:3] + word_end + ":")
print(welcome_text)
print()



intentos = 8
while intentos > 0:
    print(palabra_adivinada)
    print("Input a letter: ")
    user_letter = input()
    if user_letter in word_letters:
        #contenida
        indice = 0
        for letra in word_letters_list:
            if letra == user_letter:
                palabra_adivinada_list[indice] = user_letter
            indice += 1
        intentos -= 1
    else:
        #no contenida
        print(not_in_word)
        print()
        intentos -= 1



#
# tries = set{}
# attempts: tries.add(letra)


# print("You survived!" if palabra_adivinada == word else "You lost!")
print("""Thanks for playing!
We'll see how well you did in the next stage""")