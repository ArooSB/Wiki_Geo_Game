import countries
import artjom
import display_counter
import formatsummary
import milos
from colorama import Fore
from art import text2art


NUM_OF_ROUNDS = 5

def main():
    list_of_countries = countries.get_all_countries()  # Milos
    total_score = 0
    print(Fore.MAGENTA + f"{text2art('  wisdom', font='big')}")
    print(Fore.CYAN + f"{text2art('warriors', font='big')}")
    print(Fore.GREEN + "Welcome to Wisdom Warriors, a challenging geography trivia quiz!")
    print(Fore.BLUE + f"You will be asked {NUM_OF_ROUNDS} questions\nAre you ready?\nLET'S GO!!!")
    for _ in range(NUM_OF_ROUNDS):  # Ahmed
        # country_tuple = fetch_summary(list_of_countries)  # Aroosha
        countries_description = formatsummary.pick_country_and_format_summary(list_of_countries)
        
        # bad_answers = get_bad_answers(cleaned_country_tuple[0])  # Milos
        bad_countries =  milos.gen_bad_answers(countries_description[0], list_of_countries)
    
        score = artjom.play_one_round(countries_description, bad_countries)
        # score = play_one_round(cleaned_country_tuple, bad_answers)  # Artjom
        total_score += score


    display_counter.display_score(total_score, NUM_OF_ROUNDS) # return print out of the score.
    artjom.repeating_game()

if __name__ == "__main__":
    main()