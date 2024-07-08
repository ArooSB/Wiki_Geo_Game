import random
from colorama import Fore
import main

def play_one_round(input_tuple, bad_answers):
  country_name, trivia_text = input_tuple
  correct_answer = country_name
  all_answers = bad_answers + [correct_answer]
  random.shuffle(all_answers)

  def print_prompt():
    #create a better question label
    print(Fore.WHITE + "\nWhat country is being talked about?\n")
    print(trivia_text)
    print(f"\nChoose the correct answer from the following options:\n")
    for i, answer in enumerate(all_answers):
      print(f"{i + 1}. {answer}")

  def process_user_choice():
    positive_answer_words = ["Correct!", "Perfect!", "Awesome!", "Great!"]
    try:
      user_choice = int(input(Fore.YELLOW + f"\nEnter the number of your choice: \n")) - 1
      if all_answers[user_choice] == correct_answer:
        print(Fore.GREEN + random.choice(positive_answer_words))
        return 1
      else:
        print(Fore.RED + f"\nUnfortunately, the correct answer was - {correct_answer}.")
        return 0
    except (ValueError, IndexError):
      print(Fore.RED + f"\nInvalid input. Please enter a number from 1 to 4")
      return process_user_choice()

  print_prompt()
  return process_user_choice()




def repeating_game():
    repeat_game = input(Fore.MAGENTA + "\nDo you want to play again? (yes/no): ")
    if repeat_game.lower() == "yes":
        main.main()
    elif repeat_game.lower() == "no":
        print("\nThank you for playing!")
    else:
        print(Fore.RED + "\nInvalid input. Please enter 'yes' or 'no'.")
        repeating_game()