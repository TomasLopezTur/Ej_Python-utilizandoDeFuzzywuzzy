import random
from random import randint,choice
from fuzzywuzzy import fuzz

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Función para generar una palabra aleatoria de cuatro letras
def generate_random_word():
    return ''.join(random.choice(alphabet) for _ in range(4))

# Función para evaluar la similitud entre dos palabras
def evaluate_similarity(target, guess):
    return fuzz.ratio(target, guess)

# Pedir al usuario que ingrese una palabra de cuatro letras
target_word = input("Ingrese una palabra de cuatro letras: ")
while len(target_word) != 4:
    print("La palabra debe tener exactamente cuatro letras.")
    target_word = input("Ingrese una palabra de cuatro letras: ")

# Algoritmo genético para intentar adivinar la palabra
max_attempts = 10000
best_guess = generate_random_word()
best_score = evaluate_similarity(target_word, best_guess)

for _ in range(max_attempts):
    new_guess = generate_random_word()
    new_score = evaluate_similarity(target_word, new_guess)

    if new_score > best_score:
        best_guess = new_guess
        best_score = new_score

    if best_score == 100:
        break

print(f"Palabra objetivo: {target_word}")
print(f"Palabra adivinada: {best_guess}")