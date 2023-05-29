def calculating_number_of_digits_and_letters():
    word = input()
    digit, letter = 0, 0
    for char in word:
        digit += char.isdigit()
        letter += char.isalpha()

    print('Digit -', digit)
    print('Letter -', letter)


calculating_number_of_digits_and_letters()
