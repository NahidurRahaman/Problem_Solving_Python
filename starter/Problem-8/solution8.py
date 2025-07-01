def guessing_game():
    input_number = int(input("Enter a number 1 to 9: "))
    n = 6

    if (input_number < n):
        print("your guess is almost there")
    elif (input_number > n):
        print("your guess is higher")
    elif (input_number == n):
        print("Your Guess Is Correct!")


guessing_game()
