# In this project, the program has the user guess a special word in three tries

secret_word = "bffr"
correct_counter = 1
incorrect_counter = 3

# Prompting the user to input their guess and make the guess lowercase
user_guess = (input("Enter your guess: ")).lower()

# Conditional to check if the user guesses correctly or not, and printing the appropriate output
if user_guess == secret_word:
  print("Correct! You got it in", correct_counter, "tries!")
  exit()
else:
  incorrect_counter -= 1
  print("Sorry. That is incorrect. You have", incorrect_counter, "tries left.")
  if len(user_guess) > len(secret_word):
    print("Hint: Your guess is too long")
  elif len(user_guess) < len(secret_word):
    print("Hint: Your guess is too short")
  else:
    print("Hint: Your guess is the correct length")

# Second Try
user_guess = (input("Enter your guess: ")).lower()

if user_guess == secret_word:
  correct_counter += 1
  print("Correct! You got it in", correct_counter, "tries!")
  exit()
else:
  incorrect_counter -= 1
  print("Sorry. That is incorrect. You have", incorrect_counter, "tries left.")
  if len(user_guess) > len(secret_word):
    print("Hint: Your guess is too long")
  elif len(user_guess) < len(secret_word):
    print("Hint: Your guess is too short")
  else:
    print("Hint: Your guess is the correct length")

# Third Try
user_guess = (input("Enter your guess: ")).lower()

if user_guess == secret_word:
  correct_counter += 1
  print("Correct! You got it in", correct_counter, "tries!")
  
# Printing the Game over text if the user doesn't guess correctly in three tries
else:
  print("Game over! The correct word is", secret_word + ".")