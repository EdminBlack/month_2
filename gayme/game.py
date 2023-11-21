from hm import Game


words = ["python", "java", "javascript", "ruby", "csharp", "php"]
game = HangmanGame(words)
game.select_random_word()
print("ИГРАлОЧКА")
    
while not game.check_win() and not game.check_loss():
    print("Слово которе нужно угадать: ", game.display_word())
    print("Шансы до кредитки: ", game.guesses_remaining)
    guess = input("Введите букву: ").lower()
    result = game.make_guess(guess)
    print(result)