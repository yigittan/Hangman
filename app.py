import random 
from word import words

def getWord():
    word = random.choice(words)
    return word.upper()

def play(word):
    print(word)
    wordDisplay = "_ " * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 5
    fileNumber =0

    print("Selamke Oyun başlasın")
    while not guessed and tries >0 :
        with open(f"fileDrawn{fileNumber}","r") as file:
            print(file.read())
        guess = input("Lütfen bir harf veya kelime tahmin ediniz ...\n- ").upper()
        print(wordDisplay)
        with open(f"fileDrawn{fileNumber}","r") as file:
            print(file.read())
        if len(guess)==1 and guess.isalpha():
            if guess in guessedLetters:
                print("Bu kelimeyi daha önce tahmin ettiniz")
            elif guess not in word:
                tries -=1
                fileNumber +=1
                guessedLetters.append(guess)
                print("Denedğiniz harf kelimemizin içinde yok ...")
            else : 
                print("Bu har kelimede var :)")
                guessedLetters.append(guess)
                wordAsArray = list(wordDisplay)
                indices = [i for i , letter in enumerate(word) if letter == guess]
                for index in indices:
                    wordAsArray[index] =guess
                wordDisplay="".join(wordAsArray)
                if "_" not in wordDisplay:
                    guessed = True
        elif len(guess) ==len(word) and guess.isalpha():
            if guess ==word:
                guessed = True
                wordDisplay = word
            elif guess in guessedWords:
                print("Bu kelimeyi daha önce tahmin etmiştiniz ")
            else:
                print("Bu kelime aradğımız kelime değil")
                guessedWords.append(guess)
                tries -=1
                fileNumber +=1
        else:
            print("geçersiz tahmin")
        print(wordDisplay)
        print("\n")

    if guessed:
        with open("fileDrawn6","r") as file2:
            print(file2.read())
        print("Tebrikler doğru bildiniz ...")
    else:
        with open("fileDrawn5","r") as file3:
            print(file3.read())
        print("Malesef olmadı")

def main():
    word = getWord()
    play(word)

main()

