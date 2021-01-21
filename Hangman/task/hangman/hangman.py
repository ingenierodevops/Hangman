from random import choice

# Write your code here
word_list = ('python', 'java', 'kotlin', 'javascript')

#welcome_text= """H A N G M A N
#Guess the word """

welcome_text = "H A N G M A N"
not_in_word = "That letter doesn't appear in the word"

greeting = """Thanks for playing!
We'll see how well you did in the next stage"""
no_avances = "No improvements"

#word = "python"
word = choice(word_list)
word_letters = set(word)
word_letters_list = list(word)

#word_end = "-" * (len(word) - 3)

palabra_adivinada = "-" * (len(word))
palabra_adivinada_list = list(palabra_adivinada)
letras_intentadas = []

#print(welcome_text + word[:3] + word_end + ":")

print(welcome_text)
print()



intentos = 8
while intentos > 0:
    print(palabra_adivinada)
#    print("Input a letter: ")
    print('Input a letter: ', end="")
    user_letter = input()
    if user_letter in letras_intentadas and user_letter in word_letters:
        print(no_avances)
        intentos -= 1
        if intentos != 0 :
            print()
        continue
    else:
        letras_intentadas.append(user_letter)

    if user_letter in word_letters:
        #contenida
        indice = 0
        for letra in word_letters_list:
            if letra == user_letter:
                palabra_adivinada_list[indice] = user_letter
                # print("adivinada")
                # print(palabra_adivinada_list)
                palabra_adivinada = "".join(palabra_adivinada_list)
            indice += 1
    else:
        #no contenida
        print(not_in_word)
        intentos -= 1
    if intentos != 0 :
        print()


#
# tries = set{}
# attempts: tries.add(letra)

guessed = """You guessed the word!
You survived!"""
print(guessed if palabra_adivinada == word else "You lost!")
# print(greeting)